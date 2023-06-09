import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_SK = os.getenv('DJANGO_SK')
TZ = os.getenv('TZ')

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')
REDIS_USER = os.getenv('REDIS_USER')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

TOKEN_LIFETIME = int(os.getenv('TOKEN_LIFETIME'))
DJANGO_DEBUG = int(os.getenv('DJANGO_DEBUG'))
