from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

User.add_to_class("__str__", lambda self: self.first_name + ' ' + self.last_name)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=100, blank=True)
    pic = models.ImageField(null=True, blank=True, upload_to='profile_pictures/%Y%m/')
    phone = models.CharField(max_length=13, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pic:
            img = Image.open(self.pic.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.pic.path)

    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(
        'blog.Profile', on_delete=models.CASCADE, related_name='profile_status')
    status_message = models.CharField(max_length=160, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)
