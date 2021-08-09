from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from posts.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def create_first_post(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(title=f'Hello I\'m {UserProfile.user.username}!',
                            slug=f'first-post-of-{UserProfile.user.id}',
                            text='Nice to meet you!',
                            user=UserProfile.user)
