from datetime import datetime

from django.utils.timesince import timesince
from rest_framework import serializers
from timeline.reactions.models import Reaction, UserReaction
from timeline.posts.models import Post
from timeline.comments.models import Comment


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        depth = 1
        fields = ('name', 'emoji',)


class UserPostReactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    reaction = serializers.SlugRelatedField(queryset=Reaction.objects.all(), slug_field='emoji')
    user_full_name = serializers.SerializerMethodField()
    when = serializers.SerializerMethodField()

    class Meta:
        model = UserReaction
        fields = ('id', 'user', 'user_full_name', 'reaction', 'post', 'when')
        ordering = ('-id',)

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

    def get_when(self, instance):
        now = datetime.now().astimezone()
        time_delta = timesince(instance.created_date, now)
        return f'{time_delta} ago.'


class UserCommentReactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), write_only=True)
    reaction = serializers.SlugRelatedField(queryset=Reaction.objects.all(), slug_field='emoji')
    user_full_name = serializers.SerializerMethodField()
    when = serializers.SerializerMethodField()

    class Meta:
        model = UserReaction
        fields = ('id', 'user', 'user_full_name', 'reaction', 'comment', 'when')
        extra_kwargs = {'created_date': {'read_only': True}}

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

    def get_when(self, instance):
        now = datetime.now().astimezone()
        time_delta = timesince(instance.created_date, now)
        return f'{time_delta} ago.'
