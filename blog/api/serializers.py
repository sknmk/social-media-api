from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['slug', 'title', 'text', 'author']
        read_only_fields = ['id', 'created_date', 'author', 'comments']

    def get_time_since_pub(self, object):
        now = datetime.now().astimezone()
        if object.published_date:
            time_delta = timesince(object.published_date, now)
            return time_delta + ' ago.'
        else:
            return 'Post is not published yet.'

    def validate_published_date(self, published_date):
        today = published_date.today()
        if published_date < today:
            raise serializers.ValidationError('Invalid publish date.')
        return published_date
