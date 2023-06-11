from random import choices
from django.utils.baseconv import BASE62_ALPHABET

from urls.models import Token

CHARS = BASE62_ALPHABET

menu = [
    {'title': 'Main', 'url_name': 'main'},
    {'title': 'URLs List', 'url_name': 'token_list'},
]


def create_short_url():
    """Create a short URL token """

    while True:
        short_url = ''.join(choices(CHARS, k=6))
        if Token.objects.filter(short_url=short_url).exists():
            continue
        return short_url


def check_short_url(full_url):
    """
    Check whether the link is already shortened
    by checking last 6 chars of passed original URL
    """

    short_url = full_url[-6:]
    return Token.objects.filter(short_url=short_url).exists()
