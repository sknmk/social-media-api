from django.utils.timesince import timesince
from django.utils import timezone
from rest_framework import serializers
from timeline.posts.models import Post
from timeline.comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_full_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    time_since_published = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_date', 'user', 'comments', 'user_full_name', 'time_since_published']
        ordering = ['-id']

    def get_time_since_published(self, instance):
        now = timezone.now().astimezone()
        if instance.published_date:
            time_delta = timesince(instance.published_date, now)
            return f'{time_delta} ago.'
        else:
            return 'Post is not published yet.'

    def get_user_full_name(self, comment):
        return comment.user.get_full_name()

    def validate_published_date(self, published_date):
        if not published_date:
            return None
        now = timezone.now()
        if published_date < now:
            raise serializers.ValidationError('Invalid publish date.')
        return published_date
