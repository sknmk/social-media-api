from django.db import models
from django.utils import timezone

from django.conf import settings


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.text[0:25]
