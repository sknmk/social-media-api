from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from timeline.permissions import IsOwnerOrReadOnly
from timeline.pagination import SmallPagination
from timeline.posts.models import Post
from timeline.posts.serializers import PostSerializer
from timeline.posts.filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAdminUser|IsOwnerOrReadOnly,)
    pagination_class = SmallPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_class = PostFilter
    ordering_fields = ('published_date',)<
    search_fields = ('^title',)
