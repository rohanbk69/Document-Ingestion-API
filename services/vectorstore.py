from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct,VectorParams,Distance
import uuid

client=QdrantClient(
    url="http://localhost:6333"
)

COLLECTION='documents'

def create_collection(vector_size: int):
    collections=client.get_collections().collections
    existing=[c.name for c in collections]
    
    if COLLECTION not in existing:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

def store_vectors(chunks,embeddings):
    
    create_collection(len(embeddings[0]))
    
    points=[]
    
    for chunk,vector in zip(chunks,embeddings):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    'text':chunk.page_content,
                    'chunk_id':str(uuid.uuid4()),
                    'source':'uploaded_file'
                }
            )
        )
    client.upsert(
        collection_name=COLLECTION,
        points=points
    )