from urls.utils import check_short_url
from rest_framework import serializers


def check_original_url_validator(value):
    if check_short_url(value):
        raise serializers.ValidationError('This link is already shortened')
    return value
