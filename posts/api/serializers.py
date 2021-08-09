from datetime import datetime, timezone
import pytz
from django.utils.timesince import timesince
from rest_framework import serializers
from posts.models import Post
from comments.api.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_date', 'user', 'comments']
        ordering = ['-id']

    def get_time_since_pub(self, instance):
        now = datetime.now().astimezone()
        if instance.published_date:
            time_delta = timesince(instance.published_date, now)
            return time_delta + ' ago.'
        else:
            return 'Post is not published yet.'

    def validate_published_date(self, published_date):
        if not published_date:
            return None
        now = datetime.now(pytz.timezone('Europe/Istanbul'))
        if published_date < now:
            raise serializers.ValidationError('Invalid publish date.')
        return published_date
