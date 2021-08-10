from rest_framework import viewsets, response, status
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from rest_framework.exceptions import AuthenticationFailed
from comments.api.serializers import CommentSerializer
from api.permissions import IsAdminOrIsSelfOrReadOnly
from api.pagination import SmallPagination


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['post_id']
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        post_id = self.request.query_params.get('post_id')
        if not post_id:
            message = {'message': 'post_id is required query parameter for GET method.'}
            return response.Response(message, status=status.HTTP_400_BAD_REQUEST)
        page = self.paginate_queryset(self.queryset.filter(post_id=post_id))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return response.Response(serializer.data)
