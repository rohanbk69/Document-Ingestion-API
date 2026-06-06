from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader=PyPDFLoader(file_path)
    
    docs=loader.load()
    
    text='\n'.join(doc.page_content for doc in docs)
    
    return text

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()