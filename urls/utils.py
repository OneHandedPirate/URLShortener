from string import ascii_letters, digits
from random import choices

from urls.models import Token

CHARS = ascii_letters + digits

menu = [
    {'title': 'Main', 'url': 'token_create'},
    {'title': 'URLs List', 'url': 'token_list'},
]


def create_short_url():
    while True:
        short_url = ''.join(choices(CHARS, k=6))
        if Token.objects.filter(short_url=short_url).exists():
            continue
        return short_url
