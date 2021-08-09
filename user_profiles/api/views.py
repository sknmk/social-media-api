from rest_framework import viewsets
from rest_framework.generics import mixins
from api.permissions import IsAdminOrIsSelfOrReadOnly
from user_profiles.models import UserProfile
from user_profiles.api.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
