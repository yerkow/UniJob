from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/home', response_class=HTMLResponse)
def serve_html():
    with open(r'C:\Users\xsd\Desktop\UniJob-main\syte\resume\index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content