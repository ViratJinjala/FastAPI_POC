import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
load_dotenv()
 
DATABASE_URL = "postgresql://postgres:admin@localhost/fastapi"
 
Base = declarative_base()
engine = create_engine(DATABASE_URL,echo=True)
Session = sessionmaker(bind=engine,autoflush=False,autocommit=False)
 

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close() 