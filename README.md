# llm-site
Python backend (RAG + LLM) that powers the AI chat assistant on the CaptureMoment website. Serverless, deployed on Vercel, powered by Groq.
## Guide
```shell
# Update embeddings
python -m  rag.retrieval

# Run local server
uvicorn api.index:app --reload   
```