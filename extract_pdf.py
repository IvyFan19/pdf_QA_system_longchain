from langchain.document_loaders import PyPDFLoader
"""
S2: Extract Text from a PDF
"""

def load_pdf(file_path):
    """Loads a PDF file and extracts its text."""
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages

# Test with a sample PDF
if __name__ == "__main__":
    pdf_path = "Tax_Guide_for_Small_Business.pdf"
    documents = load_pdf(pdf_path)
    
    # Print the text from the first page
    print(f"Extracted text from Page 1:\n{documents[0].page_content}")

