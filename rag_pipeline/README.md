# RAG Pipeline for Epilepsy Research Papers

This directory contains a complete RAG (Retrieval Augmented Generation) pipeline for processing and querying your epilepsy research papers.

## Structure

```
rag_pipeline/
├── extractors/          # PDF text extraction logic
│   ├── __init__.py
│   └── pdf_extractor.py # PDFExtractor and MetadataExtractor classes
├── database/            # Database management
│   ├── __init__.py
│   └── rag_database.py  # RAGDatabase and QueryProcessor classes
├── utils/               # Utility functions
│   ├── __init__.py
│   └── helpers.py       # Logging, environment, file utilities
├── pipeline.py          # Main orchestrator class
├── interactive_query.py # Interactive CLI for querying
└── .env.example        # Environment variables template
```

## Quick Start

1. **Install dependencies:**
```bash
pip install -r ../requirements.txt
```

2. **Set up OpenAI API key:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

3. **Run the pipeline:**
```bash
# From the rag_pipeline directory
python interactive_query.py
```

## Usage Examples

### Programmatic Usage

```python
from pipeline import RAGPipeline

# Initialize pipeline
pipeline = RAGPipeline(
    papers_directory="../Papers",
    db_path="./chroma_db"
)

# Build database from PDFs
pipeline.build_database()

# Query about wearables
response = pipeline.query_wearables(
    "What types of wearable sensors are most effective for seizure detection?"
)
print(response)

# Custom query
response = pipeline.custom_query(
    "What are the main challenges in continuous epilepsy monitoring?"
)
print(response)
```

### Interactive Usage

Run `python interactive_query.py` for an interactive session where you can:
- Query about wearables information
- Ask about research methodologies
- Explore challenges and limitations
- Ask custom questions
- View database statistics

## Features

- **PDF Processing**: Extracts text from academic papers with metadata preservation
- **Intelligent Chunking**: Splits documents optimally for retrieval
- **Vector Search**: Uses ChromaDB for efficient similarity search
- **OpenAI Integration**: Leverages GPT-4 for intelligent responses
- **Specialized Queries**: Pre-built queries for wearables, methodology, and challenges
- **Interactive Interface**: CLI for easy exploration of your research

## Configuration

The pipeline can be customized by modifying parameters in the `RAGPipeline` class:

- `chunk_size`: Size of text chunks (default: 1024)
- `chunk_overlap`: Overlap between chunks (default: 200)
- `embedding_model`: OpenAI embedding model
- `llm_model`: OpenAI language model
- `collection_name`: Name for document collection

## Troubleshooting

- **Missing API Key**: Ensure `OPENAI_API_KEY` is set in your environment
- **No PDFs Found**: Check that your Papers directory contains PDF files
- **Import Errors**: Run `pip install -r ../requirements.txt`
- **Database Issues**: Try resetting the database using option 6 in interactive mode
