from django.db import models
from django.utils import timezone


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        'posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text