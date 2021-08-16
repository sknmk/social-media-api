from django.db import models
from django.conf import settings
from django.utils import timezone


class PostManager(models.Manager):
    def published_posts(self):
        return self.filter(published_date__lte=timezone.now()).order_by('published_date')


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    objects = PostManager()

    def __str__(self):
        return self.title
