from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
SesionLocal = sessionmaker(bind=engine)
Base = declarative_base()
Asanali = declarative_base()
def db_get():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

