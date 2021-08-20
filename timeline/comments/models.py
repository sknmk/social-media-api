from django.db import models
from django.conf import settings
from django.utils import timezone
from timeline.posts.models import Post


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    reactions = models.ManyToManyField('reactions.Reaction', through='reactions.UserReaction',
                                       through_fields=('comment', 'reaction',), related_name='comments')
    created_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.text[0:25]
