from rest_framework import serializers

from timeline.comments.models import Comment
from timeline.posts.models import Post
from timeline.reactions.serializers import UserReactionSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_full_name = serializers.SerializerMethodField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    user_reactions = UserReactionSerializer(many=True, read_only=True)

    def get_user_full_name(self, comment):
        return comment.user.get_full_name()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'user_full_name', 'text', 'created_date', 'post', 'user_reactions' )
        extra_kwargs = {'created_date': {'read_only': True}}
        ordering = ('-id',)
