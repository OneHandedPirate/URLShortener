from random import choices
from django.utils.baseconv import BASE62_ALPHABET

from urls.models import Token

CHARS = BASE62_ALPHABET

menu = [
    {'title': 'Main', 'url_name': 'token_create'},
    {'title': 'URLs List', 'url_name': 'token_list'},
]


def create_short_url():
    while True:
        short_url = ''.join(choices(CHARS, k=6))
        if Token.objects.filter(short_url=short_url).exists():
            continue
        return short_url
