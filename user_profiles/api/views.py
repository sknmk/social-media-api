from rest_framework import status, viewsets
from api.permissions import IsAdminOrIsSelfOrReadOnly
from user_profiles.models import UserProfile
from user_profiles.api.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = ['user_id']
    permission_classes = [IsAdminOrIsSelfOrReadOnly]
