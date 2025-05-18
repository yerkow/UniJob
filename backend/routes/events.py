from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

@router.get('/fairs', response_class=HTMLResponse)
def serve_fairs():
    html_path = static_dir / 'fairs' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

@router.get('/activities', response_class=HTMLResponse)
def serve_activities():
    html_path = static_dir / 'activities' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()