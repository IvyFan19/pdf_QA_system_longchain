

"""
S4: use LangChain’s RetrievalQA to allow users to ask questions about the PDF.
"""
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def load_vector_store():
    """Loads the FAISS vector store."""
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vector_store

def create_qa_chain():
    """Creates a question-answering chain using the vector store."""
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever()
    
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    return qa_chain

if __name__ == "__main__":
    qa_chain = create_qa_chain()
    
    while True:
        query = input("\nAsk a question about the PDF (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = qa_chain.invoke({"query": query})
        print("\nAnswer:", response)
