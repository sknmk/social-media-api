import datetime

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from rest_framework import exceptions

from model_mommy import mommy
from timeline.posts.models import Post
from timeline.reactions.serializers import ReactionSerializer, UserPostReactionSerializer, UserCommentReactionSerializer
from timeline.reactions.models import Reaction
from timeline.comments.models import Comment


class ReactionSerializerTestCase(TestCase):
    serializer_class = ReactionSerializer
    username = 'test'
    password = '123456'

    def setUp(self):
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))

    def test_reaction_serializer(self):
        data = {'name': 'Like', 'emoji': '👍'}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())


class UserPostReactionSerializerTestCase(TestCase):
    post_serializer_class = UserPostReactionSerializer
    comment_serializer_class = UserCommentReactionSerializer
    username = 'test'
    password = '123456'

    def setUp(self):
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self.post = mommy.make(Post, user=self.user, published_date=timezone.now())
        self.comment = mommy.make(Comment, user=self.user, post=self.post)
        self.reaction = mommy.make(Reaction)

    def test_serializer_valid_post_reaction(self):
        data = {'post': self.post.id, 'reaction': self.reaction.emoji}
        factory = RequestFactory().get('/')
        factory.user = self.user

        # check for post reactions serializer
        serializer = self.post_serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        expected_dict = {'id': 1,
                         'user_full_name': '',
                         'reaction': self.reaction.emoji,
                         'when': '0\xa0minutes ago.'
                         }
        self.assertDictEqual(serializer.data, expected_dict)
        # check for comment reactions serializer
        data = {'comment': self.comment.id, 'reaction': self.reaction.emoji}
        serializer = self.comment_serializer_class(data=data, context={'request': factory})
        self.assertTrue(serializer.is_valid())
        serializer.save()
        expected_dict = {'id': 2,
                         'user_full_name': '',
                         'reaction': self.reaction.emoji,
                         'when': '0\xa0minutes ago.'
                         }
        self.assertDictEqual(serializer.data, expected_dict)

    def test_serializer_invalid_post(self):
        data = {'post': '', 'reaction': self.reaction.emoji}
        factory = RequestFactory().get('/')
        factory.user = self.user
        serializer = self.post_serializer_class(data=data, context={'request': factory})
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)

        data = {'comment': self.comment.id, 'reaction': ''}
        serializer = self.comment_serializer_class(data=data, context={'request': factory})
        with self.assertRaises(exceptions.ValidationError):
            serializer.is_valid(raise_exception=True)
