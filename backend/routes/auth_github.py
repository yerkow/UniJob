from dotenv import load_dotenv
import json
import os
from jose import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
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

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

def createJwtToken(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": expire
    })
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, access_token=ALGORITHM)
    return encode_jwt

@router.get('/auth/github/login')
async def login(request: Request, type: str = 'user'):
    redirect_uri = request.url_for('auth_github_callback')
    # print (redirect_uri)
    request.session['reg_type'] = type
    return await oauth.github.authorize_redirect(request, redirect_uri)

@router.get('/auth/github/callback', name='auth_github_callback')
async def auth(request: Request):
    token = await oauth.github.authorize_access_token(request)
    user = await oauth.github.get('user', token=token)
    user_info = user.json()
    jwt_data = {
        "sub": user_info["login"],
        "name": user_info["name"],
        "login": user_info["login"],    
        "avatar": user_info.get("avatar_url"),  
        "type": "github_user"    
    }
    access_token = createJwtToken(jwt_data)
    username = user_info.get("login")
    folder = "users" 
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{username}.json"
    with open(filename, 'w', encoding='utf-8')as f:
        json.dump(user_info, f, indent=4, ensure_ascii=False)
    
    response = RedirectResponse(url='/sprofile')
    response.set_cookie(key="access_token", value=f"Bearer{access_token}", httponly=True)
    return response
