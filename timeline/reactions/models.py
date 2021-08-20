from django.db import models
from django.conf import settings
from django.utils import timezone


class Reaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=1)

    def __str__(self):
        return self.emoji


class UserReaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='user_reactions', null=True)
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, related_name='user_reactions', null=True)
    reaction = models.ForeignKey('reactions.Reaction', on_delete=models.CASCADE, related_name='user_reactions')
    created_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = (('user', 'post',), ('user', 'comment',))

    def __str__(self):
        return self.reaction.name
