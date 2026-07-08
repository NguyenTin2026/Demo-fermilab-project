# Demo Fermilab RAG Project

A lightweight Streamlit demo of a Retrieval-Augmented Generation (RAG) chatbot
over a Fermilab news/knowledge corpus.

This build is tuned to run on **Streamlit Community Cloud (CPU, no GPU)**:

- **Model:** `Qwen/Qwen2.5-0.5B-Instruct` (small, CPU-friendly) — downloaded
  automatically on first run.
- **Retrieval:** BM25 keyword search over `corpus_st7.jsonl` (2,231 chunks,
  slimmed so every chunk fits in memory). No GPU or embedding model required.

## Deploy on Streamlit Cloud

1. Push this repo to GitHub (already done).
2. On https://share.streamlit.io, create a new app pointing at this repo.
3. Set **Main file path** to `app.py`.
4. Deploy. First launch downloads the model (~1 GB) and may take a few minutes.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI + chat/generation logic |
| `retriever.py` | BM25 hybrid retriever |
| `corpus_st7.jsonl` | Knowledge corpus (slimmed to ~15 MB) |
| `train_qa.jsonl` | QA pairs used for grounding/comparison views |
| `requirements.txt` | Python dependencies (CPU-only PyTorch) |

## Notes

- The full project trains a fine-tuned Qwen3-4B model, which needs a GPU and is
  too large for Streamlit Cloud. This demo falls back to the small base model so
  it stays responsive on free CPU hardware. Answer quality is lower than the
  fine-tuned model but the app runs anywhere.
