"""
PDF Document Extractor for Academic Papers
Handles extraction of text from PDF files with metadata preservation
"""

import os
import logging
from typing import List, Dict, Optional
from pathlib import Path

from llama_index.core import Document
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter


class PDFExtractor:
    """Extracts and processes PDF documents for RAG pipeline"""
    
    def __init__(self, chunk_size: int = 1024, chunk_overlap: int = 200):
        """
        Initialize PDF extractor
        
        Args:
            chunk_size: Size of text chunks for processing
            chunk_overlap: Overlap between consecutive chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.pdf_reader = PDFReader()
        self.text_splitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        self.logger = logging.getLogger(__name__)
        
    def extract_from_file(self, file_path: str) -> List[Document]:
        """
        Extract text from a single PDF file
        
        Args:
            file_path: Path to PDF file
            
        Returns:
            List of Document objects with extracted content
        """
        try:
            # Load document
            documents = self.pdf_reader.load_data(file=Path(file_path))
            
            # Add metadata
            for doc in documents:
                doc.metadata.update({
                    'file_path': file_path,
                    'file_name': os.path.basename(file_path),
                    'source_type': 'pdf',
                    'extraction_method': 'llama_index_pdf_reader'
                })
                
            self.logger.info(f"Successfully extracted {len(documents)} documents from {file_path}")
            return documents
            
        except Exception as e:
            self.logger.error(f"Error extracting from {file_path}: {str(e)}")
            return []
    
    def extract_from_directory(self, directory_path: str, file_pattern: str = "*.pdf") -> List[Document]:
        """
        Extract text from all PDF files in a directory
        
        Args:
            directory_path: Path to directory containing PDFs
            file_pattern: File pattern to match (default: "*.pdf")
            
        Returns:
            List of all Document objects from all PDFs
        """
        directory = Path(directory_path)
        all_documents = []
        
        pdf_files = list(directory.glob(file_pattern))
        self.logger.info(f"Found {len(pdf_files)} PDF files in {directory_path}")
        
        for pdf_file in pdf_files:
            documents = self.extract_from_file(str(pdf_file))
            all_documents.extend(documents)
            
        return all_documents
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks for better retrieval
        
        Args:
            documents: List of Document objects to chunk
            
        Returns:
            List of chunked Document objects
        """
        chunked_docs = []
        
        for doc in documents:
            # Split the document into nodes/chunks
            nodes = self.text_splitter.get_nodes_from_documents([doc])
            
            # Convert nodes back to documents with preserved metadata
            for i, node in enumerate(nodes):
                chunked_doc = Document(
                    text=node.text,
                    metadata={
                        **doc.metadata,
                        'chunk_id': i,
                        'total_chunks': len(nodes),
                        'chunk_size': len(node.text)
                    }
                )
                chunked_docs.append(chunked_doc)
                
        self.logger.info(f"Created {len(chunked_docs)} chunks from {len(documents)} documents")
        return chunked_docs
    
    def extract_and_chunk(self, source_path: str, is_directory: bool = True) -> List[Document]:
        """
        Complete extraction and chunking workflow
        
        Args:
            source_path: Path to PDF file or directory
            is_directory: Whether source_path is a directory or single file
            
        Returns:
            List of chunked Document objects ready for indexing
        """
        # Extract documents
        if is_directory:
            documents = self.extract_from_directory(source_path)
        else:
            documents = self.extract_from_file(source_path)
            
        if not documents:
            self.logger.warning("No documents extracted")
            return []
            
        # Chunk documents
        chunked_documents = self.chunk_documents(documents)
        
        self.logger.info(f"Extraction complete: {len(chunked_documents)} chunks ready for indexing")
        return chunked_documents


class MetadataExtractor:
    """Extracts and enriches metadata from academic papers"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def extract_paper_metadata(self, document: Document) -> Dict:
        """
        Extract academic paper metadata from document
        
        Args:
            document: Document object to analyze
            
        Returns:
            Dictionary of extracted metadata
        """
        metadata = {
            'title': self._extract_title(document.text),
            'authors': self._extract_authors(document.text),
            'abstract': self._extract_abstract(document.text),
            'keywords': self._extract_keywords(document.text),
            'year': self._extract_year(document.metadata.get('file_name', '')),
            'file_name': document.metadata.get('file_name', ''),
        }
        
        return {k: v for k, v in metadata.items() if v}  # Remove None values
    
    def _extract_title(self, text: str) -> Optional[str]:
        """Extract title from document text"""
        lines = text.strip().split('\n')
        # Look for title in first few lines
        for line in lines[:10]:
            line = line.strip()
            if len(line) > 10 and not line.isupper() and '.' not in line:
                return line
        return None
    
    def _extract_authors(self, text: str) -> Optional[List[str]]:
        """Extract authors from document text"""
        # Simple heuristic - look for patterns like "Author1, Author2"
        # This is a simplified version - you might want to use more sophisticated methods
        return None
    
    def _extract_abstract(self, text: str) -> Optional[str]:
        """Extract abstract from document text"""
        text_lower = text.lower()
        abstract_start = text_lower.find('abstract')
        if abstract_start != -1:
            # Find the end of abstract (usually before "introduction" or "keywords")
            abstract_text = text[abstract_start:]
            for end_marker in ['introduction', 'keywords', '1.', '\n\n\n']:
                end_pos = abstract_text.lower().find(end_marker.lower())
                if end_pos != -1:
                    return abstract_text[:end_pos].replace('abstract', '').strip()
        return None
    
    def _extract_keywords(self, text: str) -> Optional[List[str]]:
        """Extract keywords from document text"""
        text_lower = text.lower()
        keywords_start = text_lower.find('keywords')
        if keywords_start != -1:
            # Extract keywords section
            keywords_section = text[keywords_start:keywords_start+500]  # Look in next 500 chars
            # Simple extraction - split by commas
            if ':' in keywords_section:
                keywords_text = keywords_section.split(':', 1)[1].strip()
                return [kw.strip() for kw in keywords_text.split(',')[:10]]  # Max 10 keywords
        return None
    
    def _extract_year(self, filename: str) -> Optional[int]:
        """Extract publication year from filename"""
        import re
        # Look for 4-digit year in filename
        year_match = re.search(r'(19|20)\d{2}', filename)
        if year_match:
            return int(year_match.group())
        return None
