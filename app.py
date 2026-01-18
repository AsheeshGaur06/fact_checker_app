import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.extract_claims import extract_claims
from utils.verify_claims import verify_claim

st.set_page_config(
    page_title="AI Fact Checker",
    layout="wide"
)

st.title("AI Fact-Checking Web App")
st.write("Upload a PDF to automatically verify numerical and factual claims.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])


def clean_text(text: str) -> str:
    replacements = {
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "²": "^2"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        text = clean_text(text)  

    with st.spinner("Extracting factual claims..."):
        claims = extract_claims(text)

    st.subheader("Fact-Check Results")

    if not claims:
        st.warning("No factual claims detected.")
    else:
        for idx, c in enumerate(claims, start=1):
            result = verify_claim(c["claim"], c["claimed_value"])

            st.markdown(f"### Claim {idx}")
            st.markdown(f"""
**Claim:** {c['claim']}  
**Claimed Value:** {c['claimed_value']}  
**Correct Value:** {result['correct_value']}  
**Status:** {result['status']}  
**Explanation:** {result['explanation']}  
**Source:** {result['source']}
""")
