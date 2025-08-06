import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page_num, page in enumerate(doc):
            page_text = page.get_text()
            if page_text.strip():
                text += f"\n\n--- Page {page_num+1} ---\n\n" + page_text
    except Exception as e:
        text = f"❌ Error reading PDF: {str(e)}"
    return text
