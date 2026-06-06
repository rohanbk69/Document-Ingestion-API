from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

def load_pdf(file_path):
    loader=PyPDFLoader(file_path)
    
    docs=loader.load()
    
    return docs

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text= f.read()
        
        return [
            Document(
                page_content=text,
                metadata={'source':file_path}
            )
        ]