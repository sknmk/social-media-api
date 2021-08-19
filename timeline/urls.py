from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from timeline.posts.views import PostViewSet
from timeline.comments.views import CommentViewSet
from timeline.reactions.views import UserPostReactionsViewSet, UserCommentReactionsViewSet
from timeline.users.views import UserProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'user/profile', UserProfileViewSet, basename='user_profile')

posts_router = nested_routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet)
posts_router.register(r'reactions', UserPostReactionsViewSet, basename='post_reactions')

comments_router = nested_routers.NestedSimpleRouter(posts_router, r'comments', lookup='comment')
comments_router.register(r'reactions', UserCommentReactionsViewSet, basename='comment_reactions')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(posts_router.urls)),
    url(r'^', include(comments_router.urls)),
]
