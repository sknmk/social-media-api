from django.utils import timezone
from rest_framework import viewsets
from api.permissions import IsAdminOrIsSelfOrReadOnly
from api.pagination import SmallPagination
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
