from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from api.permissions import IsAdminOrIsSelfOrReadOnly
from api.pagination import SmallPagination
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
    pagination_class = SmallPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
