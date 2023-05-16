from datetime import timedelta

from rest_framework import serializers
from rest_framework.reverse import reverse

from URLShortener.settings import TOKEN_LIFETIME
from urls.models import Token
from urls.utils import create_short_url


class TokenCreateSerializer(serializers.ModelSerializer):
    full_short_url = serializers.SerializerMethodField(read_only=True)
    expiration_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Token
        fields = ('original_url', 'short_url', 'full_short_url', 'created_at', 'expiration_time', 'requests_count', )
        read_only_fields = ('requests_count', 'short_url',)

    def create(self, validated_data):
        original_url = validated_data['original_url']
        token, created = Token.objects.get_or_create(original_url=original_url)
        if created:
            token.short_url = create_short_url()
            token.save()
        return token

    def get_expiration_time(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return obj.created_at + timedelta(days=TOKEN_LIFETIME)

    def get_full_short_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        return reverse('short_url_redirect', kwargs={'short_url': obj.short_url}, request=request)

