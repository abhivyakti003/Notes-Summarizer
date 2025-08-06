import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text

st.set_page_config(page_title="📄 AI Notes Summarizer", layout="wide")
st.title("📄 AI-Powered Notes Summarizer")

st.markdown("""
Welcome to the **AI-Powered Notes Summarizer**. Upload a PDF or paste any text to get a concise summary instantly using OpenAI-powered models.
""")

uploaded_file = st.file_uploader("📤 Upload a PDF file", type=["pdf"])
text_input = st.text_area("📝 Or paste some text here manually", height=300)

if uploaded_file or text_input:
    with st.spinner("⚙️ Summarizing... Please wait"):
        raw_text = extract_text_from_pdf(uploaded_file) if uploaded_file else text_input

        if raw_text.strip() == "":
            st.error("❌ No text found to summarize.")
        else:
            summary = summarize_text(raw_text)
            st.subheader("📌 Summary")
            st.write(summary)
