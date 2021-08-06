from rest_framework import serializers
from user_profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    pic = serializers.ImageField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfilePictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['pic']
