import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from users.google_auth import google_auth

load_dotenv()

SECRET_KEY = '5e932fc89b06940630d9cdb4eaf3135b0dee70bd7dce035721496d73281826d3'  # os.getenv('SECRET_KEY')

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

app.include_router(google_auth, prefix='/google', tags=['Auth'])

origins = [
    'http://localhost:9000',
    'http://127.0.0.1:9000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)