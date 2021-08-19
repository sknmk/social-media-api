from rest_framework import serializers
from django.contrib.auth.models import User
import phonenumbers
from timeline.users.models import UserProfile


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
