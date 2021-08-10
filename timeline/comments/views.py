from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from timeline.comments.models import Comment
from timeline.comments.serializers import CommentSerializer
from timeline.comments.filters import CommentFilter
from timeline.permissions import IsOwnerOrReadOnly
from timeline.pagination import SmallPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentFilter
    permission_classes = (permissions.IsAdminUser | IsOwnerOrReadOnly,)
    pagination_class = SmallPagination

