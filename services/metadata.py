from sqlalchemy import (create_engine,Column,Integer,String)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///C:/Users/ACER/OneDrive/Desktop/RAG_with_langchain/DocumentIngestionAPI/sqlite.db"

engine=create_engine(DATABASE_URL)

Session=sessionmaker(bind=engine)

Base=declarative_base()

class DocumentMetadata(Base):
    __tablename__='documents'
    id=Column(Integer,primary_key=True)
    filename=Column(String)
    chunking_strategy=Column(String)
    total_chunks=Column(Integer)
    
Base.metadata.create_all(engine)

# Save Metadata 

def save_metadata(filename,strategy,total_chunks):
    session=Session()
    try:
        data=DocumentMetadata(
            filename=filename,
            chunking_strategy=strategy,
            total_chunks=total_chunks
        )
        session.add(data)
        session.commit()
    except Exception as e:
        session.rollback()
        print('Error:',e)
    finally:
        session.close()