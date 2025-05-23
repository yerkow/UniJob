from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()
static_dir = Path(__file__).parent.parent.parent / 'syte'

#лаваня страницы
@router.get('/', response_class=HTMLResponse)
def rollan():
    print('Rollan')