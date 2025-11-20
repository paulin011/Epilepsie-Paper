def get_pdf_files(folder_path):
    import os
    return [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

def save_markdown_file(content, file_path):
    with open(file_path, 'w') as md_file:
        md_file.write(content)

def convert_pdf_to_markdown(pdf_path):
    # Placeholder for PDF to Markdown conversion logic
    return f"# Converted content from {pdf_path}"