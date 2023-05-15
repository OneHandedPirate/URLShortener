from django.db import models


class Token(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=6, db_index=True, unique=True)
    requests_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url


