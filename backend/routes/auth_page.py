from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

#Страница входа
@router.get('/auth', response_class=HTMLResponse)
def serve_auth():
    html_path = static_dir / 'auth' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()  