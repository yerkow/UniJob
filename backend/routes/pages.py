from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

@router.get('/', response_class=HTMLResponse)
def serve_home():
    html_path = static_dir / 'home' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

@router.get('/home', response_class=HTMLResponse)
def serve_resume():
    html_path = static_dir / 'resume' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

@router.get('/sprofile', response_class=HTMLResponse)
def serve_profile():
    html_path = static_dir / 'profile' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()