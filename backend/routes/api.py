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

#Меню поиск вакансии
@app.get('/jobfinder', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'jobfinder' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

#Меню Отклики и приглашения
@app.get('/responses', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'responses' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

#Меню Дни карьеры
@app.get('/fairs', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'fairs' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

#Меню События
@app.get('/activities', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'activities' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

#Меню Курсы
@app.get('/courses', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'courses' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

# Меню Тестирования
@app.get('/tests', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'tests' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

# Меню СКБ
@app.get('/skblist', response_class=HTMLResponse)
def server_profile():
    html_path = static_dir / 'skblist' / 'index.html'
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content