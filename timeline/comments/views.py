from rest_framework import viewsets, permissions
from rest_framework.generics import mixins
from django_filters.rest_framework import DjangoFilterBackend

from timeline.comments.models import Comment
from timeline.comments.serializers import CommentSerializer
from timeline.pagination import SmallPagination


class CommentViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    pagination_class = SmallPagination

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])
