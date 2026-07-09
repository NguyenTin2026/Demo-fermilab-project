# Demo Fermilab RAG Project

A lightweight Streamlit demo of a Retrieval-Augmented Generation (RAG) chatbot
over a Fermilab news/knowledge corpus.

This build is tuned to run on **Streamlit Community Cloud (CPU, ~1 GB RAM)**:

- **Answer generation:** the **Anthropic API** (`claude-haiku-4-5`). No local LLM
  is loaded — a local model would exceed Cloud's memory limit and crash the app
  ("Oh no. Error running app."). Set an `ANTHROPIC_API_KEY` to enable it (below).
- **Retrieval:** BM25 keyword search over `corpus_st7.jsonl` (2,231 pages,
  slimmed so every page fits in memory). No GPU or embedding model required.
- **No key?** The app still runs and shows the grounded source passage for each
  question instead of a generated answer — it never fabricates.

## Enable answers: set your Anthropic API key

On Streamlit Cloud: **Manage app → Settings → Secrets**, then add:

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

Locally: put the same line in `.streamlit/secrets.toml`, or export
`ANTHROPIC_API_KEY` as an environment variable. (Cost for a demo is a few cents.)

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
4. Add `ANTHROPIC_API_KEY` under **Settings → Secrets** (see above).
5. Deploy. The build is light (no torch/transformers), so it starts in under a minute.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI + RAG + grounding guardrail + Anthropic-API generation |
| `retriever.py` | BM25 hybrid retriever (dense reranking when embeddings are present) |
| `corpus_st7.jsonl` | Knowledge corpus (slimmed to ~15 MB, 2,231 pages) |
| `train_qa.jsonl` | QA pairs used for source pinning and grounding/comparison views |
| `FERMILAB_RAG_GROUNDED_QA.md` | 241 verified-grounded Q&A pairs (answerable only from the corpus) |
| `requirements.txt` | Python dependencies (lean; no local ML stack) |

## Notes

- The full project also trains a fine-tuned Qwen3-4B model, which needs a GPU and
  is too large for Streamlit Cloud. This demo generates through the Anthropic API
  instead, so it stays within Cloud's memory limit. The retrieval, source pinning,
  and grounding guardrail are identical either way, so answers stay tied to the
  corpus regardless of which model writes them.
- If both a GPU and `torch`/`transformers` are available (e.g. a local/SLURM run
  with no API key), `app.py` still loads the local fine-tuned model automatically.
