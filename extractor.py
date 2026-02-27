from pathlib import Path
from docx import Document
from PyPDF2 import PdfReader


TEXT_EXTENSIONS = { ".txt", ".md", ".log", ".py", ".json", ".xml", ".html", ".csv" }

def extract_text(path: str) -> str:
    """
    Determines the file type based on extension and routes the file
    to the correct extraction helper function.
    
    Parameters:
        path (str): Full file path.

    Returns:
        str: Extracted plain text, or "" if extraction fails or file type is unsupported.   
    """

    extension = Path(path).suffix.lower()

    if extension in TEXT_EXTENSIONS:
        return read_plain_text(path)
    
    if extension == ".docx":
        return extract_docx_text(path)
    
    if extension == ".pdf":
        return extract_pdf_text(path)
    
    if extension == ".doc":
        return extract_doc_text(path)

    return ""

def extract_doc_text(path: str) -> str:
    return ""

def extract_docx_text(path: str) -> str: 
    try:
        doc = Document(path)
        paragraphs = []
        for paragraph in doc.paragraphs:
            paragraphs.append(paragraph.text)
        full_text = "\n".join(paragraphs)
        return(full_text)
    except:
        return ""


def extract_pdf_text(path: str) -> str:
    try:
        reader = PdfReader(path)
        pages_text = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
        full_text = "\n".join(pages_text)
        return full_text    
    except:
        return ""

def read_plain_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""
