from datetime import timedelta

from django.contrib import admin

from .models import Token
from .utils import create_short_url


class TokenAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'expires_at', 'requests_count')
    list_filter = ('created_at',)
    search_fields = ('original_url', 'created_at')

    @staticmethod
    def expires_at(obj):
        return obj.created_at + timedelta(days=7)


admin.site.register(Token, TokenAdmin)
