from rest_framework import serializers
from django.contrib.auth.models import User
from timeline.users.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    pic = serializers.ImageField()
    # TODO: do picture file and format validations

    class Meta:
        model = UserProfile
        fields = '__all__'
