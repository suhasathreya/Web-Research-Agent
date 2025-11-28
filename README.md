# 🔎 Web Research Agent

A minimal web-research assistant powered by **Parallel Web Systems Search API** and **OpenRouter LLM** (Llama-3.3-70B-Instruct:free), wrapped in a clean **Streamlit UI**.
https://web-research-agent-ge6d8cshoqeemmszjztwj4.streamlit.app/

This app:
- Performs accurate web search using Parallel
- Extracts excerpts and metadata
- Summarizes findings using an LLM
- Runs locally (via `.env`) and on Streamlit Cloud (via `st.secrets`)

---

## 🚀 Features

- 🔍 One-shot web search (Parallel Search API)  
- 🧠 LLM summarization (OpenRouter)  
- 🖥️ Simple Streamlit interface  
- 🔐 Secure API key handling  
- 🧩 Easy to extend into multi-step agents  

---

## 🧱 Tech Stack

- Python  
- Streamlit  
- Parallel Web Systems API  
- OpenRouter API  
- Llama-3.3-70B-Instruct (free tier)

---

## 🛠️ Run Locally

### 1️⃣ Install dependencies
```bash
pip install streamlit python-dotenv requests
```

### 2️⃣ Create a .env file
```bash
OPENROUTER_API_KEY=your_key_here
PARALLEL_API_KEY=your_key_here
```

### 3️⃣ Start the app
```bash
streamlit run app.py
```
