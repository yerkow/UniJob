from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

@router.get('/jobfinder', response_class=HTMLResponse)
def serve_jobfinder():
    html_path = static_dir / 'jobfinder' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()

@router.get('/responses', response_class=HTMLResponse)
def serve_responses():
    html_path = static_dir / 'responses' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        return file.read()