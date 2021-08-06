from rest_framework import viewsets
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from api.permissions import IsAdminOrIsSelfOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = ['post_id']
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
