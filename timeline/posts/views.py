from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from timeline.pagination import SmallPagination
from timeline.permissions import IsOwnerOrReadOnly
from timeline.posts.models import Post
from timeline.posts.serializers import PostSerializer
from timeline.posts.filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('user').prefetch_related('user_reactions__reaction',
                                                                    'comments__user_reactions__reaction')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    pagination_class = SmallPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_class = PostFilter
    ordering_fields = ('published_date',)
    search_fields = ('^title',)
