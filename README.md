🔎 Web Research Agent

A simple research assistant powered by Parallel Web Systems Search API + OpenRouter LLM (Llama-3.3-70B-Instruct:free).
Built with Python + Streamlit.

This agent:

Searches the web using Parallel’s high-accuracy search API

Extracts excerpts and metadata

Summarizes findings using an LLM

Runs both locally (with .env) and on Streamlit Cloud (st.secrets)

🚀 Features

One-shot web search via Parallel

AI summarization via OpenRouter

Clean Streamlit UI

Secure local + cloud API key handling

Very easy to extend into a multi-step agent

📦 Tech Stack

Python

Streamlit

Parallel Web Systems Search API

OpenRouter API

Llama-3.3-70B-Instruct (free tier)

🛠️ Running Locally
1. Install dependencies
pip install streamlit python-dotenv requests

2. Create a .env file
OPENROUTER_API_KEY=your_key_here
PARALLEL_API_KEY=your_key_here

3. Start app
streamlit run app.py

🌐 Deploying on Streamlit Cloud

Add the API keys under:
Settings → Secrets → OPENROUTER_API_KEY, PARALLEL_API_KEY

Deploy by connecting this GitHub repo.

🧱 Folder Structure
web-agent/
│── app.py            # Streamlit UI
│── agent.py          # Parallel API + OpenRouter LLM logic
│── .env              # Local secrets (ignored by Git)
│── .gitignore

🧩 Extend This Project

Planned upgrades:

Parallel extract API

Parallel monitor API

Multi-agent pipelines

Docker + AWS deployment

📜 License

MIT License

If you want, I can generate:

✅ A prettier README
✅ A badge-style README
✅ An animated GIF demo section
✅ Deployment instructions for Docker, AWS, or Fly.io

Just tell me!
