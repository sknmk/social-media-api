from rest_framework import serializers, exceptions
from timeline.comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        exclude = ['created_date', 'is_deleted']
        ordering = ['-id']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_anonymous:
            raise exceptions.AuthenticationFailed()
        return Comment.objects.create(user=user, **validated_data)
