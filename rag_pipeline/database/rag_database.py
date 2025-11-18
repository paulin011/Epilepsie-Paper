"""
Database Manager for RAG Pipeline
Handles vector database operations with ChromaDB and LlamaIndex
"""

import os
import logging
from typing import List, Optional, Dict, Any
from pathlib import Path

from llama_index.core import VectorStoreIndex, StorageContext, Settings, Document
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import chromadb


class RAGDatabase:
    """Manages the RAG database with ChromaDB backend"""
    
    def __init__(self, 
                 db_path: str = "./chroma_db",
                 collection_name: str = "epilepsy_papers",
                 embedding_model: str = "text-embedding-3-small",
                 # Default to an OpenRouter-compatible model name; can be overridden via env or args
                 llm_model: str = "openrouter/openai/gpt-4.1-mini"):
        """
        Initialize RAG database
        
        Args:
            db_path: Path to store ChromaDB files
            collection_name: Name of the ChromaDB collection
            embedding_model: OpenAI/OpenRouter embedding model to use
            llm_model: OpenAI/OpenRouter LLM model to use
        """
        self.db_path = db_path
        self.collection_name = collection_name
        self.logger = logging.getLogger(__name__)
        
        # Allow overriding models via environment variables if desired
        embedding_model = os.getenv("EMBEDDING_MODEL", embedding_model)
        llm_model = os.getenv("LLM_MODEL", llm_model)
        
        # Setup LlamaIndex settings (these will use OPENAI_API_KEY and OPENAI_BASE_URL)
        Settings.embed_model = OpenAIEmbedding(model=embedding_model)
        Settings.llm = OpenAI(model=llm_model)
        
        # Initialize ChromaDB
        self._initialize_database()
        
    def _initialize_database(self):
        """Initialize ChromaDB client and collection"""
        try:
            # Create database directory if it doesn't exist
            os.makedirs(self.db_path, exist_ok=True)
            
            # Initialize ChromaDB client
            self.chroma_client = chromadb.PersistentClient(path=self.db_path)
            
            # Get or create collection
            self.chroma_collection = self.chroma_client.get_or_create_collection(
                name=self.collection_name
            )
            
            # Create vector store
            self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
            self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
            
            self.logger.info(f"Database initialized at {self.db_path}")
            
        except Exception as e:
            self.logger.error(f"Error initializing database: {str(e)}")
            raise
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the vector database
        
        Args:
            documents: List of Document objects to add
        """
        try:
            if not documents:
                self.logger.warning("No documents to add")
                return
                
            # Create or update index
            if hasattr(self, 'index'):
                # Add to existing index
                for doc in documents:
                    self.index.insert(doc)
            else:
                # Create new index
                self.index = VectorStoreIndex.from_documents(
                    documents, 
                    storage_context=self.storage_context
                )
            
            self.logger.info(f"Added {len(documents)} documents to database")
            
        except Exception as e:
            self.logger.error(f"Error adding documents: {str(e)}")
            raise
    
    def get_query_engine(self, **kwargs):
        """
        Get query engine for RAG queries
        
        Args:
            **kwargs: Additional arguments for query engine configuration
            
        Returns:
            Query engine object
        """
        if not hasattr(self, 'index'):
            raise ValueError("No index found. Add documents first.")
            
        # Default query engine parameters
        query_params = {
            'similarity_top_k': kwargs.get('top_k', 5),
            'response_mode': kwargs.get('response_mode', 'compact'),
            'streaming': kwargs.get('streaming', False)
        }
        
        return self.index.as_query_engine(**query_params)
    
    def query(self, query_text: str, **kwargs) -> str:
        """
        Query the RAG database
        
        Args:
            query_text: Question or query to ask
            **kwargs: Additional query parameters
            
        Returns:
            Response from the RAG system
        """
        try:
            query_engine = self.get_query_engine(**kwargs)
            response = query_engine.query(query_text)
            return str(response)
            
        except Exception as e:
            self.logger.error(f"Error during query: {str(e)}")
            raise
    
    def get_collection_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the current collection
        
        Returns:
            Dictionary with collection statistics
        """
        try:
            count = self.chroma_collection.count()
            return {
                'collection_name': self.collection_name,
                'document_count': count,
                'db_path': self.db_path
            }
        except Exception as e:
            self.logger.error(f"Error getting stats: {str(e)}")
            return {}
    
    def delete_collection(self):
        """Delete the current collection"""
        try:
            self.chroma_client.delete_collection(name=self.collection_name)
            self.logger.info(f"Deleted collection: {self.collection_name}")
        except Exception as e:
            self.logger.error(f"Error deleting collection: {str(e)}")
            raise
    
    def list_collections(self) -> List[str]:
        """List all collections in the database"""
        try:
            collections = self.chroma_client.list_collections()
            return [col.name for col in collections]
        except Exception as e:
            self.logger.error(f"Error listing collections: {str(e)}")
            return []


class QueryProcessor:
    """Processes and enhances queries for better RAG results"""
    
    def __init__(self, database: RAGDatabase):
        self.database = database
        self.logger = logging.getLogger(__name__)
    
    def query_about_wearables(self, specific_question: Optional[str] = None) -> str:
        """
        Query specifically about wearables in the papers
        
        Args:
            specific_question: Specific question about wearables, or None for general overview
            
        Returns:
            Response about wearables
        """
        if specific_question:
            query = f"Based on the research papers, {specific_question} Specifically focus on wearable devices, sensors, and monitoring technology."
        else:
            query = """
            What information is available about wearable devices for epilepsy monitoring and seizure detection? 
            Please provide details about:
            1. Types of wearable sensors mentioned
            2. Monitoring capabilities
            3. Effectiveness and accuracy
            4. Practical considerations for patients
            5. Future developments or recommendations
            """
        
        return self.database.query(query, top_k=8)
    
    def query_about_methodology(self) -> str:
        """Query about research methodologies used in the papers"""
        query = """
        What research methodologies and approaches are described in these papers for 
        studying epilepsy monitoring and wearable devices? Include information about 
        study designs, data collection methods, and evaluation metrics.
        """
        return self.database.query(query, top_k=6)
    
    def query_about_challenges(self) -> str:
        """Query about challenges and limitations mentioned in the papers"""
        query = """
        What challenges, limitations, and future research directions are discussed 
        in these papers regarding wearable devices for epilepsy monitoring?
        """
        return self.database.query(query, top_k=6)
    
    def custom_query(self, query_text: str, context: str = "epilepsy research") -> str:
        """
        Process a custom query with context
        
        Args:
            query_text: The user's question
            context: Context to add to the query
            
        Returns:
            Response to the query
        """
        enhanced_query = f"In the context of {context}: {query_text}"
        return self.database.query(enhanced_query)
