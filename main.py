from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
import shutil
import os
import uuid

from services.chunker import *
from services.embeddings import *
from services.loader import *
from services.metadata import *
from services.vectorstore import *

app=FastAPI()

@app.post('/upload')

async def upload_document(
    file:UploadFile=File(...),
    strategy:str='recursive'
):
    os.makedirs('uploads',exist_ok=True)
    
    unique_name=f'{uuid.uuid4()}_{file.filename}'
    path=os.path.join('uploads',unique_name)
    
    with open(path,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)
        
    if file.filename.endswith('.pdf'):
        text=load_pdf(path)
        
    else:
        text=load_txt(path)
        
    if strategy=='semantic':
        chunks=semantic_chunk(text)
        
    else:
        chunks=recursive_chunk(text)
        
    texts=[
        chunk.page_content for chunk in chunks
    ]
    
    embeddings=create_embeddings(texts)
    
    assert len(chunks)==len(embeddings)
    
    store_vectors(chunks,embeddings)
    
    save_metadata(
        file.filename,
        strategy,
        len(chunks)
        
    )
    
    return{
        'filename':file.filename,
        'chunks':len(chunks),
        'strategy':strategy
    }