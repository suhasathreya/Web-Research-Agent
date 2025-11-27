import streamlit as st
from agent import parallel_search, summarize_with_llm

st.title("🔎 Simple Web Research Agent")

query = st.text_input("Enter your research question:")

if st.button("Run Research"):
    with st.spinner("Searching the web with Parallel..."):
        search_output = parallel_search(query)

    with st.expander("📄 Show Search Evidence", expanded=False):
        st.text(search_output)

    with st.spinner("Summarizing with Llama 3.3 70B..."):
        summary = summarize_with_llm(query, search_output)

    st.subheader("📝 Final Summary")
    st.write(summary)
