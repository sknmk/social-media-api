from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from rest_framework import exceptions

from model_mommy import mommy
from timeline.comments.serializers import CommentSerializer
from timeline.posts.models import Post


class CommentSerializerTestCase(TestCase):
    serializer_class = CommentSerializer
    username = 'test'
    password = '123456'

    def setUp(self):
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self.post = mommy.make(Post, user=self.user, published_date=timezone.now())

    def test_serializer_valid_comment(self):
        data = {'text': 'Test comment', 'post': self.post.id}
        created_date = timezone.now()
        data['created_date'] = created_date
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
        serializer.save()

        expected_dict = {'user_full_name': '',
                         'text': 'Test comment',
                         'created_date': serializer.data['created_date'],
                         'post': self.post.pk
                         }
        self.assertDictEqual(serializer.data, expected_dict)

    def test_serializer_invalid_post(self):
        data = {'text': '', 'post': self.post.id}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
