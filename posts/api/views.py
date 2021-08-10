from django.utils import timezone
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import AuthenticationFailed
from api.permissions import IsAdminOrIsSelfOrReadOnly
from api.pagination import SmallPagination
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
    pagination_class = SmallPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['published_date']
    search_fields = ['^title']

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return serializer.save(user=self.request.user)
