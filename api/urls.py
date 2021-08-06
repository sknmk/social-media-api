from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='dashboard'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post/publish/<int:pk>/', views.post_publish, name='post_publish'),
    path('post/drafts', views.post_drafts, name='post_drafts'),
    path('post/<int:pk>/comment/', views.comment_new, name='comment_new'),
    path('post/<int:fk>/comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('post/<int:fk>/comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('api/', include('blog.api.urls')),
]
