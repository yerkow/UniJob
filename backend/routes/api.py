from fastapi import FastAPI
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from .pages import router as pages_router
from .jobs import router as jobs_router
from .events import router as events_router
from .edu import router as edu_router
from .auth_page import router as auth_router

app = FastAPI()

# Монтируем статику один раз — на всю папку syte
static_dir = Path(__file__).parent.parent.parent / 'syte'
app.mount("/static", StaticFiles(directory=static_dir), name='static')
app.include_router(pages_router)
app.include_router(jobs_router)
app.include_router(events_router)
app.include_router(edu_router)
app.include_router(auth_router)
