from celery import shared_task

from .models import Token


@shared_task
def delete_token_task(token_id):
    """Delete a token"""
    Token.objects.filter(pk=token_id).delete()
    return f'Token with ID {token_id} is deleted'
