
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from extract_pdf import load_pdf
from dotenv import load_dotenv

"""
S3: Convert PDF Text into Embeddings for Retrieval
"""
# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def create_vector_store(file_path):
    """Loads a PDF, converts text into embeddings, and stores them in FAISS."""
    # Load PDF text
    documents = load_pdf(file_path)

    # Initialize OpenAI Embeddings
    embeddings = OpenAIEmbeddings()

    # Store embeddings in FAISS vector database
    vector_store = FAISS.from_documents(documents, embeddings)

    # Save the FAISS index
    vector_store.save_local("faiss_index")

    print("✅ Embeddings created and stored successfully!")

if __name__ == "__main__":
    pdf_path = "Tax_Guide_for_Small_Business.pdf"  
    create_vector_store(pdf_path)
