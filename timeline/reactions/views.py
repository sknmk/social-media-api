from rest_framework import viewsets, permissions
from rest_framework.generics import mixins
from django_filters.rest_framework import DjangoFilterBackend

from timeline.reactions.models import UserReaction
from timeline.reactions.serializers import UserReactionSerializer, UserCommentReactionSerializer
from timeline.pagination import SmallPagination
from timeline.permissions import IsOwnerOrReadOnly


class UserPostReactionsViewSet(mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.CreateModelMixin,
                               viewsets.GenericViewSet):
    queryset = UserReaction.objects.all()
    serializer_class = UserReactionSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = SmallPagination

    def get_queryset(self):
        return super().get_queryset().filter(post=self.kwargs['post_pk'])


class UserCommentReactionsViewSet(mixins.ListModelMixin,
                                  mixins.DestroyModelMixin,
                                  mixins.CreateModelMixin,
                                  viewsets.GenericViewSet):
    queryset = UserReaction.objects.all()
    serializer_class = UserCommentReactionSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = SmallPagination

    def get_queryset(self):
        return super().get_queryset().filter(comment=self.kwargs['comment_pk'])
