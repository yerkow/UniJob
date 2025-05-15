from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Монтируем статику один раз — на всю папку syte
static_dir = Path(__file__).parent.parent.parent / 'syte'
app.mount("/static", StaticFiles(directory=static_dir), name='static')

@app.get('/', response_class=HTMLResponse)
def serve_home():
    html_path = static_dir / 'home' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

@app.get('/home', response_class=HTMLResponse)
def serve_resume():
    html_path = static_dir / 'resume' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

@app.get('/sprofile', response_class=HTMLResponse)
def serve_profile():
    html_path = static_dir / 'profile' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content