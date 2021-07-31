from django.urls import path
from blog.api import views as api_views

urlpatterns = [
    path('list/', api_views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>', api_views.PostDetail.as_view(), name='post_detail'),
    path('detail/<int:pk>/comments', api_views.PostComment.as_view(), name='post_comment'),
]
