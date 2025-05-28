from fastapi import FastAPI, Form, Depends, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import os
from .pages import router as pages_router
from .jobs import router as jobs_router
from .events import router as events_router
from .edu import router as edu_router
from .auth_page import router as auth_router
from .auth_github import router as auth_github
from .students_api import router as student_api

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key= os.getenv("SECRET_KEY"))
# Монтируем статику один раз — на всю папку syte
static_dir = Path(__file__).parent.parent.parent / 'syte'
app.mount("/static", StaticFiles(directory=static_dir), name='static')
app.include_router(pages_router)
app.include_router(jobs_router)
app.include_router(events_router)
app.include_router(edu_router)
app.include_router(auth_router)
app.include_router(auth_github)
app.include_router(student_api)