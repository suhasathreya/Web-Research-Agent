import os
import requests
# Attempt Streamlit Cloud secrets first
try:
    import streamlit as st
    OPENROUTER_KEY = st.secrets["OPENROUTER_API_KEY"]
    PARALLEL_KEY  = st.secrets["PARALLEL_API_KEY"]
    print("[INFO] Loaded API keys from Streamlit Cloud secrets.")
except:
    # Local fallback using .env
    from dotenv import load_dotenv
    load_dotenv()
    OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
    PARALLEL_KEY  = os.getenv("PARALLEL_API_KEY")
    print("[INFO] Loaded API keys from local .env")

def parallel_search(query):
    url = "https://api.parallel.ai/v1beta/search"
    headers = {
        "Authorization": f"Bearer {PARALLEL_KEY}",
        "Content-Type": "application/json",
        "parallel-beta": "search-extract-2025-10-10"
    }

    payload = {
        "mode": "one-shot",
        "objective": query,
        "search_queries": [query],
        "max_results": 5
    }

    print("\n[DEBUG] Sending request to Parallel...")
    print("[DEBUG] Headers:", headers)
    print("[DEBUG] Payload:", payload)

    try:
        response = requests.post(url, json=payload, headers=headers)
        print("[DEBUG] Status Code:", response.status_code)
        print("[DEBUG] Raw Response:", response.text)
    except Exception as e:
        print("[ERROR] Exception occurred:", e)
        return "ERROR: request failed"

    try:
        data = response.json()
    except Exception as e:
        print("[ERROR] Failed to parse JSON:", e)
        return "ERROR: JSON parse failed"

    results = []
    for item in data.get("results", []):
        excerpts = item.get("excerpts", [])
        excerpt_text = " ".join(excerpts) if excerpts else "[No excerpts available]"

        results.append(f"- {item.get('title')} ({item.get('url')})\n{excerpt_text}")

    if not results:
        return "[DEBUG] No results returned."

    return "\n\n".join(results)


# -------------------------------------------
# LLM SUMMARIZATION (OPENROUTER)
# -------------------------------------------
def summarize_with_llm(query, search_results):
    prompt = f"""
            You are a research AI.
            The user asked: "{query}"

            Here is the retrieved information:

            {search_results}

            Write a clear, factual summary.
            Include references using the URLs from the search results.
            """

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "My Research Agent"
    }

    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers
        )
        data = response.json()

        choice = data.get("choices", [{}])[0]
        message = choice.get("message", {})
        content = message.get("content", "")

        return content

    except Exception as e:
        return f"[ERROR] LLM failed: {e}"

if __name__ == "__main__":
    print("Testing parallel_search...\n")
    query = "What is Parallel Web Systems?"
    out = parallel_search(query)
    print(out)

    print("Testing LLM summarization")
    summary = summarize_with_llm(query, out)
    print(summary)
