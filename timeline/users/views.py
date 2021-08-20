from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.generics import mixins

from timeline.permissions import IsOwnerOrReadOnly
from timeline.users.models import UserProfile
from timeline.users.serializers import UserProfileSerializer
from timeline.users.serializers import UserSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = UserProfile.objects.select_related('user')
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
