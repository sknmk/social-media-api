"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from posts.api.views import PostViewSet
from comments.api.views import CommentViewSet
from user_profiles.api.views import UserProfileViewSet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'user/profile', UserProfileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/basic-auth/', include('rest_framework.urls')),
    url(r'^api/token-auth/', include('rest_auth.urls')),
    url(r'^api/token-auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router.urls
