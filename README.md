# Demo Fermilab RAG Project

A lightweight Streamlit demo of a Retrieval-Augmented Generation (RAG) chatbot
over a Fermilab news/knowledge corpus.

This build is tuned to run on **Streamlit Community Cloud (CPU, no GPU)**:

- **Model:** `Qwen/Qwen2.5-0.5B-Instruct` (small, CPU-friendly) — downloaded
  automatically on first run.
- **Retrieval:** BM25 keyword search over `corpus_st7.jsonl` (2,231 pages,
  slimmed so every page fits in memory). No GPU or embedding model required.

## Grounding: answers come only from the corpus

The demo is built so replies stay **grounded in the provided documents** and do
not fabricate information:

- **Source pinning.** Every training question (`train_qa.jsonl`) — and two
  hand-verified demo questions (NOvA, SeaQuest) — is mapped to the exact corpus
  page it was written from. That page is fetched and placed first in the context,
  so the model always sees the correct evidence.
- **Strict prompt.** The system prompt instructs the model to *"answer using
  ONLY the provided context"* and to *"not use outside knowledge, invent facts,
  or guess beyond the text."*
- **Refusal guardrail.** When the retrieved documents genuinely do not cover a
  question, the app replies *"I don't know from the current Fermilab corpus"*
  instead of guessing. The guardrail was tuned so it no longer refuses valid,
  well-covered questions (including instruction-style phrasings).

The full list of questions that are verified answerable **only** from the corpus
is in [`FERMILAB_RAG_GROUNDED_QA.md`](FERMILAB_RAG_GROUNDED_QA.md) — 241 Q&A
pairs with an average answer-to-source coverage of **0.92**.

### Suggested demo questions

- What does Fermilab's NOvA experiment study?
- What did the SeaQuest experiment measure?
- What did the Tevatron discover?
- Why is CERN's contribution to the DUNE experiment considered significant?
- What is the primary purpose of the PIP-II linear accelerator at Fermilab?
- What is the Quantum Instrumentation Control Kit (QICK) developed by Fermilab?

## Deploy on Streamlit Cloud

1. Push this repo to GitHub (already done).
2. On https://share.streamlit.io, create a new app pointing at this repo.
3. Set **Main file path** to `app.py`.
4. Deploy. First launch downloads the model (~1 GB) and may take a few minutes.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI + chat/generation logic + grounding guardrail |
| `retriever.py` | BM25 hybrid retriever (dense reranking when embeddings are present) |
| `corpus_st7.jsonl` | Knowledge corpus (slimmed to ~15 MB, 2,231 pages) |
| `train_qa.jsonl` | QA pairs used for source pinning and grounding/comparison views |
| `FERMILAB_RAG_GROUNDED_QA.md` | 241 verified-grounded Q&A pairs (answerable only from the corpus) |
| `requirements.txt` | Python dependencies (CPU-only PyTorch) |

## Notes

- The full project trains a fine-tuned Qwen3-4B model, which needs a GPU and is
  too large for Streamlit Cloud. This demo falls back to the small base model so
  it stays responsive on free CPU hardware. Answer quality is lower than the
  fine-tuned model, but the retrieval, source pinning, and grounding guardrail
  are identical, so answers stay tied to the corpus regardless of the model.
