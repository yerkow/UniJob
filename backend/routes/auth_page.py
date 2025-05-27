from fastapi import APIRouter, Form, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
from sqlalchemy.orm import Session
from ..database.connectDB import Base, engine, db_get, Asanali
from ..database.models import User, UserCreate
from pydantic import ValidationError
from .untils import hashFunction
Base.metadata.create_all(bind=engine)
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
async def register_user(request: Request ,data: UserCreate ,db: Session = Depends(db_get)):
    body = await request.json()
    print(body)

    hash = hashFunction(data.password)
    newUser = User(email= data.email, hashed_password= hash, first_name= data.name, last_name= data.surname, types= data.type)
    db.add(newUser)
    db.commit()
    return RedirectResponse(url="/sprofile", status_code=307)
