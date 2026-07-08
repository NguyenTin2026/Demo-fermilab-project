#!/usr/bin/env python3
import json
import math
import re
import os
from pathlib import Path
import numpy as np

class Retriever:
    def __init__(self, corpus_path="corpus_st7.jsonl", k1=1.5, b=0.75, rrf_k=60):
        self.k1 = k1
        self.b = b
        self.rrf_k = rrf_k
        self.documents = []
        self.doc_len = []
        self.doc_term_freqs = []
        self.df = {}
        self.avg_doc_len = 0.0
        
        # Paths setup
        self.base_dir = Path(__file__).parent
        self.corpus_file = self.base_dir / corpus_path if not Path(corpus_path).is_absolute() else Path(corpus_path)
        if not self.corpus_file.exists():
            # Fallback to local working directory
            self.corpus_file = Path(corpus_path)
            if not self.corpus_file.exists():
                raise FileNotFoundError(f"Corpus file not found: {corpus_path}")

        print(f"Loading corpus from {self.corpus_file}...")
        try:
            with open(self.corpus_file, "r", encoding="utf-8") as f:
                for line_number, raw_line in enumerate(f, 1):
                    line = raw_line.strip()
                    if not line:
                        continue
                    if line.startswith("version https://git-lfs.github.com/spec/v1"):
                        print("Corpus file looks like a Git LFS pointer rather than JSONL data. No documents were loaded.")
                        break
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as exc:
                        print(f"Skipping invalid JSONL line {line_number}: {exc}")
                        continue
                    if isinstance(record, dict):
                        self.documents.append(record)
                    else:
                        print(f"Skipping malformed document at line {line_number}")
        except Exception as exc:
            print(f"Failed to read corpus file: {exc}")
        
        self.n_docs = len(self.documents)
        print(f"Loaded {self.n_docs} chunks. Indexing BM25...")
        
        total_len = 0
        for doc in self.documents:
            tokens = self._tokenize(doc["text"])
            self.doc_len.append(len(tokens))
            total_len += len(tokens)
            
            tf = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            self.doc_term_freqs.append(tf)
            
            for t in tf.keys():
                self.df[t] = self.df.get(t, 0) + 1
                
        self.avg_doc_len = total_len / self.n_docs if self.n_docs > 0 else 1.0
        
        # Dense Retrieval Setup (CPU-friendly)
        self.embeddings_path = self.corpus_file.parent / "corpus_embeddings.npy"
        self.model = None
        self.doc_embeddings = None
        
        self._load_or_compute_embeddings()

    def _tokenize(self, text):
        return re.findall(r"\b[a-z0-9]{2,}\b", text.lower())

    def _load_or_compute_embeddings(self):
        """Loads pre-computed embeddings or computes them using SentenceTransformer on CPU."""
        if self.n_docs == 0:
            print("No corpus documents available; skipping embedding initialization.")
            self.doc_embeddings = np.empty((0, 0), dtype=np.float32)
            return

        if self.doc_embeddings is not None:
            # Already loaded and validated.
            pass
        elif self.embeddings_path.exists():
            print(f"Loading pre-computed semantic embeddings from {self.embeddings_path}...")
            try:
                loaded = np.load(str(self.embeddings_path))
                if loaded.ndim == 2 and loaded.shape[0] == self.n_docs:
                    self.doc_embeddings = loaded
                else:
                    print(f"Cached embeddings shape {getattr(loaded, 'shape', None)} does not match corpus size {self.n_docs}; recomputing.")
                    self.doc_embeddings = None
            except Exception as exc:
                print(f"Failed to load cached embeddings: {exc}; recomputing.")
                self.doc_embeddings = None

        if self.doc_embeddings is None:
            print("No pre-computed embeddings found. Initializing SentenceTransformer on CPU...")
            try:
                from sentence_transformers import SentenceTransformer
                # Small, fast model: ~90MB, 384 dimensions
                self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
                
                print("Encoding corpus chunks (this runs once and caches the result)...")
                texts = [doc["text"] for doc in self.documents]
                # Encode in batches
                self.doc_embeddings = self.model.encode(texts, batch_size=64, show_progress_bar=True, convert_to_numpy=True)
                
                print(f"Saving corpus embeddings to {self.embeddings_path}...")
                np.save(str(self.embeddings_path), self.doc_embeddings)
            except ImportError:
                print("sentence-transformers is not installed; semantic index unavailable, falling back to BM25-only retrieval.")
                self.doc_embeddings = np.empty((0, 0), dtype=np.float32)
                return
            except Exception as exc:
                print(f"Failed to compute semantic embeddings: {exc}; falling back to BM25-only retrieval.")
                self.doc_embeddings = np.empty((0, 0), dtype=np.float32)
                return
            
        if self.doc_embeddings is None or self.doc_embeddings.size == 0:
            self.doc_embeddings = np.empty((0, 0), dtype=np.float32)
            print("Semantic index unavailable; falling back to BM25-only retrieval.")
            return

        # Normalize embeddings for fast cosine similarity via dot product
        norms = np.linalg.norm(self.doc_embeddings, axis=1, keepdims=True)
        norms[norms == 0] = 1.0  # Avoid division by zero
        self.doc_embeddings = self.doc_embeddings / norms
        print(f"Semantic index ready. Shape: {self.doc_embeddings.shape}")

    def _get_bm25_scores(self, query_tokens, split=None):
        scores = {}
        for doc_idx, tf in enumerate(self.doc_term_freqs):
            doc = self.documents[doc_idx]
            if split and doc.get("split") != split:
                continue
                
            doc_len = self.doc_len[doc_idx]
            score = 0.0
            for t in query_tokens:
                if t in tf:
                    df_t = self.df.get(t, 0)
                    idf = math.log((self.n_docs - df_t + 0.5) / (df_t + 0.5) + 1.0)
                    
                    tf_t = tf[t]
                    numerator = tf_t * (self.k1 + 1)
                    denominator = tf_t + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_doc_len))
                    score += idf * (numerator / denominator)
            if score > 0:
                scores[doc_idx] = score
        return scores

    def _get_semantic_scores(self, query, split=None):
        if self.n_docs == 0:
            return {}

        if self.doc_embeddings is None or self.doc_embeddings.size == 0:
            return {}

        # Lazy load model if not loaded yet
        if self.model is None:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
            
        # Embed query and normalize
        query_embedding = self.model.encode(query, convert_to_numpy=True)
        q_norm = np.linalg.norm(query_embedding)
        if q_norm > 0:
            query_embedding = query_embedding / q_norm
            
        # Cosine similarity is simply dot product now
        similarities = np.dot(self.doc_embeddings, query_embedding)
        
        scores = {}
        for doc_idx, sim in enumerate(similarities):
            doc = self.documents[doc_idx]
            if split and doc.get("split") != split:
                continue
            # Keep positive similarities
            if sim > 0:
                scores[doc_idx] = float(sim)
        return scores

    def retrieve(self, query: str, top_k: int = 3, split: str = None) -> list[dict]:
        """Hybrid Retrieval combining BM25 and Semantic Search using Reciprocal Rank Fusion (RRF)."""
        query_tokens = self._tokenize(query)
        
        # 1. Get BM25 rankings
        bm25_scores = self._get_bm25_scores(query_tokens, split)

        if self.doc_embeddings is None or self.doc_embeddings.size == 0:
            sorted_indices = sorted(bm25_scores.keys(), key=lambda idx: bm25_scores[idx], reverse=True)[:top_k]
            return [self._format_result(idx, bm25_scores[idx]) for idx in sorted_indices]

        # 2. Get Semantic rankings
        semantic_scores = self._get_semantic_scores(query, split)
        
        # 3. Hybrid score. Use normalized score magnitudes so an exact BM25 hit
        # like "SeaQuest" is not outranked by a semantically broad match to
        # "measure" from an unrelated document.
        hybrid_scores = {}
        all_candidates = set(bm25_scores.keys()) | set(semantic_scores.keys())
        max_bm25 = max(bm25_scores.values(), default=1.0)
        max_semantic = max(semantic_scores.values(), default=1.0)
        query_entities = self._query_entities(query)
        
        for doc_idx in all_candidates:
            score_bm25 = bm25_scores.get(doc_idx, 0.0) / max_bm25
            score_sem = semantic_scores.get(doc_idx, 0.0) / max_semantic
            hybrid_scores[doc_idx] = (0.7 * score_bm25) + (0.3 * score_sem)

            if query_entities:
                doc = self.documents[doc_idx]
                title_origin = f"{doc.get('title', '')} {doc.get('origin', '')}".lower()
                full_text = f"{title_origin} {doc.get('text', '')}".lower()
                if not all(entity in full_text for entity in query_entities):
                    hybrid_scores[doc_idx] *= 0.05
                elif any(entity in title_origin for entity in query_entities):
                    hybrid_scores[doc_idx] += 0.25
            
        # 4. Title Reranking & Boosting
        # Boost document score if query terms match the document title
        query_words = set(self._tokenize(query))
        for doc_idx in hybrid_scores.keys():
            doc = self.documents[doc_idx]
            title_words = set(self._tokenize(doc.get("title", "")))
            matches = len(query_words & title_words)
            if matches > 0:
                # Add a boost proportional to matching words
                hybrid_scores[doc_idx] += 0.02 * matches

        # Sort by hybrid score
        sorted_indices = sorted(hybrid_scores.keys(), key=lambda idx: hybrid_scores[idx], reverse=True)[:top_k]
        
        results = []
        for idx in sorted_indices:
            results.append(self._format_result(idx, hybrid_scores[idx]))
            
        return results

    def _format_result(self, idx, score):
        doc = self.documents[idx]
        return {
            "id": doc["id"],
            "text": doc["text"],
            "title": doc["title"],
            "origin": doc["origin"],
            "split": doc.get("split", ""),
            "score": round(score, 4),
        }

    def _query_entities(self, query):
        generic = {
            "what", "does", "did", "was", "were", "the", "and", "its", "biggest",
            "discovery", "experiment", "study", "measure", "measured",
        }
        entities = []
        for token in re.findall(r"\b[A-Za-z][A-Za-z0-9]*\b", query):
            if token.lower() not in generic and any(ch.isupper() for ch in token):
                entities.append(token.lower())
        return entities

if __name__ == "__main__":
    # Self-test the hybrid retriever
    try:
        ret = Retriever("corpus_st7.jsonl")
        test_queries = ["What did the SeaQuest experiment measure?", "DUNE experiment neutrino"]
        for q in test_queries:
            print(f"\nQuery: {q}")
            results = ret.retrieve(q, top_k=2)
            for r in results:
                print(f"  [{r['score']}] Title: {r['title']} | URL: {r['origin']}")
                print(f"    Text snippet: {r['text'][:150]}...")
    except Exception as e:
        print(f"Error during self-test: {e}")
