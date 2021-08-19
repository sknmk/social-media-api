import datetime

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from rest_framework import exceptions

from model_mommy import mommy
from timeline.posts.serializers import PostSerializer


class PostSerializerTestCase(TestCase):
    serializer_class = PostSerializer
    username = 'test'
    password = '123456'

    def setUp(self):
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))

    def test_serializer_valid_post(self):
        data = {'title': 'Test Title', 'slug': 'test-slug', 'text': 'Test Content', 'published_date': None}
        created_date = timezone.now()
        data['created_date'] = created_date
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
        serializer.save()

        expected_dict = {'id': 1,
                         'user_full_name': '',
                         'comments': [],
                         'time_since_published': 'Post is not published yet.',
                         'slug': 'test-slug',
                         'title': 'Test Title',
                         'reactions': [],
                         'text': 'Test Content',
                         'created_date': serializer.data['created_date'],
                         'published_date': None
                         }
        self.assertDictEqual(serializer.data, expected_dict)

    def test_serializer_invalid_post(self):
        data = {'title': 'Test Title', 'slug': 'test-slug', 'text': 'Test Content',
                'published_date': timezone.now() - datetime.timedelta(days=1)}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_correct_published_date(self):
        data = {'title': 'Test Title', 'slug': 'test-slug', 'text': 'Test Content',
                'published_date': timezone.now() + datetime.timedelta(days=1)}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
