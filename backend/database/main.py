from . import models, database
from sqlalchemy.orm import Session
from . import database, models

models.Base.metadata.create_all(bind=database.engine) 

def get_db():
    db = database.S