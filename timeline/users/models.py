from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
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
