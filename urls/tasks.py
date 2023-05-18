from celery import shared_task

from .models import Token


@shared_task
def delete_url(token_id):
    """Delete a token"""

    token = Token.objects.get(pk=token_id)
    token.delete()
    return f'{token.short_url} is deleted'
