from django.urls import path
from comments.api import views as api_views

comment_list = api_views.CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

comment_detail = api_views.CommentViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('list/<int:post_id>/', comment_list, name='comment_list'),
    path('detail/<int:pk>/', comment_detail, name='comment_detail')
]
