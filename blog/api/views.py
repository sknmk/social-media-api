from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils import timezone
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer
from blog.api.permissions import isAdminOrIsAuthorOrReadOnly
from blog.api.pagination import SmallPagination, LargePagination


class PostList(ListCreateAPIView):

    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SmallPagination

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [isAdminOrIsAuthorOrReadOnly]


class PostComment(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = ['post_id']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostCommentDetail(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [isAdminOrIsAuthorOrReadOnly]
