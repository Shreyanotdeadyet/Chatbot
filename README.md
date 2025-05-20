# Document Question Answering System with Semantic Search and LLM

This project implements a document question answering system by combining semantic search with a large language model (LLM). It enables users to ask questions about the content of raw PDF documents and receive accurate answers based on the knowledge extracted from those documents.

## Features

- Extraction of text from raw PDFs.
- Splitting text into chunks for embedding.
- Creating vector embeddings for chunks and storing them in FAISS vector store.
- Semantic search to find relevant document chunks given a user query.
- Integration with a Large Language Model to generate human-like answers from the retrieved content.

## Project Phases

### Phase 1: Knowledge Base Creation
- Input raw PDFs.
- Extract text and split into chunks.
- Convert chunks to embeddings.
- Store embeddings in FAISS vector store as the knowledge base.

### Phase 2: Query Processing
- Input a user question.
- Convert the question to an embedding.
- Perform semantic search to find relevant chunks.
- Rank and pass these chunks to the LLM.

### Phase 3: Answer Generation
- The LLM generates an answer based on the ranked results.
- Output the answer to the user.

## Setup

1. Clone the repository.

2. Install dependencies:

```bash
# Install PyTorch (CPU version) and torchvision
pip install torch==2.7.0+cpu torchvision==0.18.1+cpu --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
pip install -r requirements.txt

