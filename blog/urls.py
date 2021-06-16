from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post/publish/<int:pk>/', views.post_publish, name='post_publish'),
    path('post/drafts', views.post_drafts, name='post_drafts'),
]
