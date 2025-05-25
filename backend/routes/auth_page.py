from fastapi import APIRouter, Form, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
from sqlalchemy.orm import Session
from ..database.connectDB import Base, engine, db_get, Asanali
from ..database.models import User, UserCreate
from pydantic import ValidationError
from .untils import hashFunction
# Base.metadata.create_all(bind=engine)
# Asanali.metadata.create_all(bind=engine)

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

#Страница входа
@router.get('/auth', response_class=HTMLResponse)
def serve_auth():
    html_path = static_dir / 'auth' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()
    
@router.post('/api/register')
def register_user(name: str = Form(...), firstName:str = Form(...) , password:str= Form(...), passwordTwo:str = Form(...) , email:str = Form(...), db: Session = Depends(db_get)):
    try:
        data = UserCreate(name= name, email= email, password=password, config_password= passwordTwo)
    except ValidationError as error:
        return {"error": error.errors()}
    hash = hashFunction(data.password)
    newUser = User(name= data.name, email = data.email, hash_password = hash)
    db.add(newUser)
    db.commit()
    return RedirectResponse(url="/sprofile")
