from fastapi import APIRouter
from starlette.config import Config
from starlette.requests import Request
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth


google_auth = APIRouter()

config = Config('.env')

oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@google_auth.get('/login')
async def login(request: Request):
    redirect_url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_url)


@google_auth.route('/auth')
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token['userinfo']
    if user:
        request.session['user'] = dict(user)
        print(user)
        return RedirectResponse(url=f'http://localhost:9000/#access_token={user.sub}')


@google_auth.get('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='http://localhost:9000/login')
