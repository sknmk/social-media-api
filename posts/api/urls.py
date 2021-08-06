from django.urls import path
from posts.api import views as api_views

post_list = api_views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

post_detail = api_views.PostViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('list/', post_list, name='post_list'),
    path('detail/<int:pk>', post_detail, name='post_detail'),
]
