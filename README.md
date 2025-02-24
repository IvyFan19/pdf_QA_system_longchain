# PDF Question-Answering System using LangChain

This project implements a question-answering system for PDF documents using embeddings and language models (ChatGPT-4o).

## Features

- Extract text from PDF documents
- Create embeddings for document content
- Question-answering capability using the extracted content
- Environment variable management for API keys

## Prerequisites

- Python 3.8 or higher
- Required packages listed in `requirements.txt`

## Installation

1. Clone the repository
```
git clone https://github.com/your-repo/pdf-question-answering.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file in the root directory and add your API key:
```
OPENAI_API_KEY=your_api_key
```

## Project Structure

- `create_embeddings.py`: Creates embeddings from the extracted PDF text
- `create_qa_chain.py`: Implements the question-answering chain (Main file)
- `extract_pdf.py`: Handles PDF text extraction
- `load_api_key.py`: Manages API key loading from environment variables
- `requirements.txt`: Lists all Python dependencies

## Usage

1. Place your PDF document in the project directory
2. Run the main script:
```
python create_qa_chain.py
```
3. Ask questions about the PDF content

