from rest_framework import viewsets, permissions
from rest_framework.generics import mixins
from django_filters.rest_framework import DjangoFilterBackend

from timeline.comments.models import Comment
from timeline.comments.serializers import CommentSerializer
from timeline.pagination import SmallPagination
from timeline.permissions import IsOwnerOrReadOnly


class CommentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.select_related('user', 'post').prefetch_related('user_reactions')
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = SmallPagination

    def get_queryset(self):
        return super().get_queryset().filter(post=self.kwargs['post_pk'])
