from django.contrib.auth.models import User
from rest_framework import serializers

import phonenumbers

from timeline.users.models import UserProfile, UserFollower


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff',)
        ordering = ('-id',)


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = '__all__'
        ordering = ('-id',)

    def validate_phone(self, phone):
        if phone and not phonenumbers.is_valid_number(phonenumbers.parse(phone)):
            raise serializers.ValidationError('Invalid phone number. Please use country code for your number.')
        return phone


class UserFollowerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    following = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserFollower
        fields = '__all__'
        ordering = ('-id',)
        unique_together = ('user', 'following')

    def validate(self, attrs):
        attrs = super(UserFollowerSerializer, self).validate(attrs)
        if attrs.get('following') == attrs.get('user'):
            raise serializers.ValidationError('User and following parameters cannot be same.')
        return attrs


