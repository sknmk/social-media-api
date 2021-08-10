from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from timeline.posts.views import PostViewSet
from timeline.comments.views import CommentViewSet
from timeline.users.views import UserProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'user/profile', UserProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
