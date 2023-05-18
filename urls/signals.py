from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta

from .models import Token
from .tasks import delete_url
from URLShortener.settings import TOKEN_LIFETIME


@receiver(post_save, sender=Token)
def delete_token(sender, instance, created, **kwargs):
    """Passes token delete delayed task to celery"""

    expiration_time = instance.created_at + timedelta(days=TOKEN_LIFETIME)
    delete_url.apply_async(args=[instance.pk], eta=expiration_time)
