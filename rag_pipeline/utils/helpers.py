"""
Utility functions for the RAG pipeline
"""

import os
import logging
from typing import Optional
from pathlib import Path


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None) -> None:
    """
    Setup logging configuration
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional log file path
    """
    level = getattr(logging, log_level.upper())
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Setup handlers
    handlers = [logging.StreamHandler()]
    
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
    
    # Configure logging
    logging.basicConfig(
        level=level,
        handlers=handlers,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def load_environment() -> None:
    """Load environment variables from .env file"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        logging.warning("python-dotenv not installed. Environment variables should be set manually.")


def validate_openai_key() -> bool:
    """
    Validate that OpenAI API key is set
    
    Returns:
        True if API key is available, False otherwise
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logging.error(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in your .env file or environment."
        )
        return False
    return True


def ensure_directory(directory_path: str) -> Path:
    """
    Ensure directory exists, create if it doesn't
    
    Args:
        directory_path: Path to directory
        
    Returns:
        Path object for the directory
    """
    path = Path(directory_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_project_root() -> Path:
    """Get the project root directory"""
    return Path(__file__).parent.parent


def count_files_in_directory(directory_path: str, pattern: str = "*.pdf") -> int:
    """
    Count files matching pattern in directory
    
    Args:
        directory_path: Path to directory
        pattern: File pattern to match
        
    Returns:
        Number of matching files
    """
    directory = Path(directory_path)
    if not directory.exists():
        return 0
    return len(list(directory.glob(pattern)))


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"
