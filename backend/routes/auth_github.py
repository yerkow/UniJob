from dotenv import load_dotenv
from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth
from backend.controllers.github_controllers import encryption_request
import os 

load_dotenv()  # Загружает переменные из .env

router = APIRouter()
oauth = OAuth()
oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),         # <-- из .env
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'), # <-- из .env
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)



@router.get('/auth/github/login')
async def login(request: Request, type: str = 'user'):
    redirect_uri = request.url_for('auth_github_callback')
    # print (redirect_uri)
    request.session['reg_type'] = type
    return await oauth.github.authorize_redirect(request, redirect_uri)

@router.get('/auth/github/callback', name='auth_github_callback')
async def auth(request: Request):
    return await encryption_request(request, oauth)