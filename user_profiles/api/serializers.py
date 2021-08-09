from rest_framework import serializers
from user_profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    pic = serializers.ImageField()
    # TODO: do picture file and format validations

    class Meta:
        model = UserProfile
        fields = '__all__'
