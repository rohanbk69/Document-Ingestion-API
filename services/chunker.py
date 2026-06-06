from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

def recursive_chunk(docs):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    
    return splitter.split_documents(docs)

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def semantic_chunk(docs):
    splitter=SemanticChunker(
        embeddings
    )
    
    return splitter.split_documents(docs)