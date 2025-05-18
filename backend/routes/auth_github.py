from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth

router = APIRouter()
oauth = OAuth()
oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',           
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',   
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)
