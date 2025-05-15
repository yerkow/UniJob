from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

@app.get('/home', response_class=HTMLResponse)
def serve_html():
    # Получаем путь к index.html относительно текущего файла

    html_path = Path(__file__).parent.parent.parent / 'syte' / 'resume' / 'index.html'
    print(html_path)
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content