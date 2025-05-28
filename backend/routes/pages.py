from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from pathlib import Path
from sqlalchemy.orm import Session
from ..database.connectDB import db_get
from ..database.models import User, Student

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

#лаваня страницы
@router.get('/', response_class=HTMLResponse)
def serve_home():
    html_path = static_dir / 'home' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

# Проофиль
@router.get('/sprofile', response_class=HTMLResponse)
def serve_profile():
    html_path = static_dir / 'profile' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

# Работодатель
@router.get('/employer', response_class=HTMLResponse)
def serve_profile():
    html_path = static_dir / 'employer' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()
