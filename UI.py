import streamlit as st
from langchain_helper import explain_code_for_beginners

st.title("👶 Code Explainer for Beginners")
st.markdown("Created by **Sivaprasath Munusamy**")

code_input = st.text_area("Paste your code snippet here:", height=300)

if st.button("Explain Code"):
    if not code_input.strip():
        st.warning("Please paste some code to explain.")
    else:
        with st.spinner("Generating beginner-friendly explanation..."):
            explanation = explain_code_for_beginners(code_input)
        st.subheader("Explanation for Beginners")
        st.write(explanation)
