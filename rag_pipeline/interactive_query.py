"""
Interactive script for querying the RAG database
Run this script to interact with your research papers
"""

import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import our modules
sys.path.append(str(Path(__file__).parent))

from pipeline import RAGPipeline


def interactive_session():
    """Run an interactive session with the RAG database"""
    
    print("🧠 Epilepsy Research RAG System")
    print("=" * 50)
    
    # Initialize pipeline
    try:
        pipeline = RAGPipeline(
            papers_directory="../Papers",  # Adjust path relative to script location
            db_path="./chroma_db"
        )
        
        # Check if database exists
        stats = pipeline.get_database_stats()
        if stats.get('document_count', 0) == 0:
            print("📚 Database is empty. Building database from PDF papers...")
            pipeline.build_database()
            stats = pipeline.get_database_stats()
        
        print(f"✅ Database loaded with {stats.get('document_count', 0)} documents")
        
    except Exception as e:
        print(f"❌ Error initializing pipeline: {e}")
        print("Make sure:")
        print("1. Your Papers directory contains PDF files")
        print("2. OPENAI_API_KEY is set in your environment")
        print("3. Required packages are installed")
        return
    
    print("\n🔍 Available query types:")
    print("1. Wearables information")
    print("2. Research methodologies") 
    print("3. Challenges and limitations")
    print("4. Custom question")
    print("5. Database statistics")
    print("6. Reset database")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("\n👉 Choose option (1-6) or type your question: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            elif user_input == '1':
                print("\n🔍 Querying about wearables...")
                response = pipeline.query_wearables()
                print("\n📖 Wearables Information:")
                print("-" * 50)
                print(response)
                
            elif user_input == '2':
                print("\n🔍 Querying about methodologies...")
                response = pipeline.query_methodology()
                print("\n📖 Research Methodologies:")
                print("-" * 50)
                print(response)
                
            elif user_input == '3':
                print("\n🔍 Querying about challenges...")
                response = pipeline.query_challenges()
                print("\n📖 Challenges and Limitations:")
                print("-" * 50)
                print(response)
                
            elif user_input == '4':
                question = input("❓ Enter your question: ").strip()
                if question:
                    print(f"\n🔍 Querying: {question}")
                    response = pipeline.custom_query(question)
                    print("\n📖 Response:")
                    print("-" * 50)
                    print(response)
                    
            elif user_input == '5':
                stats = pipeline.get_database_stats()
                print("\n📊 Database Statistics:")
                print("-" * 50)
                for key, value in stats.items():
                    print(f"{key}: {value}")
                    
            elif user_input == '6':
                confirm = input("⚠️  Are you sure you want to reset the database? (yes/no): ")
                if confirm.lower() == 'yes':
                    pipeline.reset_database()
                    print("🔄 Database reset complete")
                    
            else:
                # Treat as custom question
                print(f"\n🔍 Querying: {user_input}")
                response = pipeline.custom_query(user_input)
                print("\n📖 Response:")
                print("-" * 50)
                print(response)
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again or type 'quit' to exit")


if __name__ == "__main__":
    interactive_session()
