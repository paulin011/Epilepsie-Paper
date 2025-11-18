"""
Main RAG Pipeline Workflow
Orchestrates the complete process from PDF extraction to RAG database creation
"""

import logging
from pathlib import Path
from typing import Optional, List

from .extractors import PDFExtractor, MetadataExtractor
from .database import RAGDatabase, QueryProcessor
from .utils import setup_logging, load_environment, validate_openai_key, ensure_directory


class RAGPipeline:
    """Main pipeline orchestrator for PDF processing and RAG database creation"""
    
    def __init__(self, 
                 papers_directory: str = "./Papers",
                 db_path: str = "./chroma_db",
                 collection_name: str = "epilepsy_papers",
                 chunk_size: int = 1024,
                 chunk_overlap: int = 200):
        """
        Initialize the RAG pipeline
        
        Args:
            papers_directory: Directory containing PDF papers
            db_path: Path for ChromaDB storage
            collection_name: Name for the document collection
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.papers_directory = papers_directory
        self.db_path = db_path
        self.collection_name = collection_name
        
        # Setup logging
        setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # Load environment variables
        load_environment()
        
        # Validate OpenAI API key
        if not validate_openai_key():
            raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
        
        # Initialize components
        self.pdf_extractor = PDFExtractor(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.metadata_extractor = MetadataExtractor()
        
        # Ensure directories exist
        ensure_directory(self.db_path)
        
        # Initialize database
        self.database = RAGDatabase(
            db_path=self.db_path,
            collection_name=self.collection_name
        )
        
        # Initialize query processor
        self.query_processor = QueryProcessor(self.database)
        
        self.logger.info("RAG Pipeline initialized successfully")
    
    def run_extraction(self) -> List:
        """
        Run the complete extraction process
        
        Returns:
            List of extracted and chunked documents
        """
        self.logger.info(f"Starting extraction from {self.papers_directory}")
        
        # Check if papers directory exists
        papers_path = Path(self.papers_directory)
        if not papers_path.exists():
            raise FileNotFoundError(f"Papers directory not found: {self.papers_directory}")
        
        # Extract and chunk documents
        documents = self.pdf_extractor.extract_and_chunk(
            source_path=self.papers_directory,
            is_directory=True
        )
        
        if not documents:
            self.logger.warning("No documents extracted")
            return []
        
        # Enrich with metadata
        for doc in documents:
            additional_metadata = self.metadata_extractor.extract_paper_metadata(doc)
            doc.metadata.update(additional_metadata)
        
        self.logger.info(f"Extraction complete: {len(documents)} documents processed")
        return documents
    
    def build_database(self, documents: Optional[List] = None) -> None:
        """
        Build the RAG database
        
        Args:
            documents: Optional list of documents. If None, runs extraction first.
        """
        if documents is None:
            documents = self.run_extraction()
        
        if not documents:
            self.logger.error("No documents to add to database")
            return
        
        self.logger.info("Building RAG database...")
        self.database.add_documents(documents)
        
        # Print database statistics
        stats = self.database.get_collection_stats()
        self.logger.info(f"Database built successfully: {stats}")
    
    def query_wearables(self, specific_question: Optional[str] = None) -> str:
        """
        Query about wearables information
        
        Args:
            specific_question: Specific question about wearables
            
        Returns:
            Response about wearables
        """
        return self.query_processor.query_about_wearables(specific_question)
    
    def query_methodology(self) -> str:
        """Query about research methodologies"""
        return self.query_processor.query_about_methodology()
    
    def query_challenges(self) -> str:
        """Query about challenges and limitations"""
        return self.query_processor.query_about_challenges()
    
    def custom_query(self, question: str) -> str:
        """
        Ask a custom question
        
        Args:
            question: Question to ask
            
        Returns:
            Response to the question
        """
        return self.query_processor.custom_query(question)
    
    def get_database_stats(self) -> dict:
        """Get database statistics"""
        return self.database.get_collection_stats()
    
    def reset_database(self) -> None:
        """Reset the database (delete all data)"""
        self.logger.warning("Resetting database - all data will be deleted")
        self.database.delete_collection()
        
        # Reinitialize database
        self.database = RAGDatabase(
            db_path=self.db_path,
            collection_name=self.collection_name
        )
        self.query_processor = QueryProcessor(self.database)
        
        self.logger.info("Database reset complete")


def main():
    """Main function to run the complete pipeline"""
    # Initialize pipeline
    pipeline = RAGPipeline(
        papers_directory="./Papers",
        db_path="./chroma_db"
    )
    
    # Run extraction and build database
    print("🔄 Starting RAG pipeline...")
    pipeline.build_database()
    
    # Show database stats
    stats = pipeline.get_database_stats()
    print(f"✅ Database built successfully!")
    print(f"📊 Documents in database: {stats.get('document_count', 0)}")
    
    # Example queries
    print("\n🔍 Example Queries:")
    
    print("\n1. Wearables Information:")
    print("-" * 50)
    wearables_info = pipeline.query_wearables()
    print(wearables_info[:500] + "..." if len(wearables_info) > 500 else wearables_info)
    
    print("\n2. Research Methodologies:")
    print("-" * 50)
    methodology_info = pipeline.query_methodology()
    print(methodology_info[:500] + "..." if len(methodology_info) > 500 else methodology_info)


if __name__ == "__main__":
    main()
