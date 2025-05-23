from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

#Страница курсов
@router.get('/courses', response_class=HTMLResponse)
def serve_courses():
    html_path = static_dir / 'courses' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()
#Тестировние
@router.get('/tests', response_class=HTMLResponse)
def serve_tests():
    html_path = static_dir / 'tests' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

#СКБ
@router.get('/skblist', response_class=HTMLResponse)
def serve_skblist():
    html_path = static_dir / 'skblist' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()
    
@router.get('/profile_', response_class=HTMLResponse)
def serve_skblist():
    html_path = static_dir / 'profile_' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()