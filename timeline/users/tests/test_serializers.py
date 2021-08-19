from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import exceptions
from model_mommy import mommy

from timeline.users.serializers import UserProfileSerializer


class UserProfileSerializerTestCase(TestCase):
    serializer_class = UserProfileSerializer
    username = 'test'
    password = '123456'

    def setUp(self):
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))

    def test_serializer_valid_user_profile(self):
        data = {'bio': 'Lorem ipsum dolor sit amet.', 'area': 'Istanbul, Europe', 'phone': '+905554443210'}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
        serializer.save()

        expected_dict = {'id': 1,
                         'bio': 'Lorem ipsum dolor sit amet.',
                         'area': 'Istanbul, Europe',
                         'pic': None,
                         'phone': '+905554443210'
                         }
        self.assertDictEqual(serializer.data, expected_dict)

    def test_serializer_invalid_post(self):
        data = {'bio': 'Lorem ipsum dolor sit amet.', 'area': 'Istanbul, Europe', 'phone': '+9055544432101'}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
