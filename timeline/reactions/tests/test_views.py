from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import test, status

from model_mommy import mommy
from timeline.posts.models import Post
from timeline.comments.models import Comment
from timeline.reactions.models import Reaction, UserReaction


class ReactionsViewTestCase(TestCase):
    username = 'test'
    second_username = 'test2'
    password = '123456'

    def setUp(self):
        self.client = test.APIClient()
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self._login()
        self.post = mommy.make(Post, user=self.user, published_date=timezone.now())
        self.comment = mommy.make(Comment, user=self.user, post=self.post)
        self.reaction = mommy.make(Reaction)
        self.user_post_reaction = mommy.make(UserReaction, user=self.user, post=self.post,
                                             reaction=self.reaction)
        self.user_comment_reaction = mommy.make(UserReaction, user=self.user, comment=self.comment,
                                                reaction=self.reaction)

    def test_reaction_instance(self):
        self.assertIsInstance(self.user_post_reaction, UserReaction)
        self.assertIsInstance(self.user_comment_reaction, UserReaction)

    def test_reaction_list(self):
        # post reaction
        url = reverse('post-reactions-list', kwargs={'post_pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # comment reaction
        url = reverse('comment-reactions-list', kwargs={'post_pk': self.post.pk, 'comment_pk': self.comment.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reaction_create_with_same_cred(self):
        url = reverse('post-reactions-list', kwargs={'post_pk': self.post.pk})
        response = self.client.post(path=url, data={'reaction': self.reaction.emoji, 'post': self.post.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = reverse('comment-reactions-list', kwargs={'post_pk': self.post.pk, 'comment_pk': self.comment.pk})
        response = self.client.post(path=url, data={'reaction': self.reaction.emoji, 'comment': self.comment.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reaction_create(self):
        self._logout()
        mommy.make(User, username=self.second_username, password=make_password(self.password))
        self.client.login(username=self.second_username, password=self.password)
        url = reverse('post-reactions-list', kwargs={'post_pk': self.post.pk})
        response = self.client.post(path=url, data={'reaction': self.reaction.emoji, 'post': self.post.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('comment-reactions-list', kwargs={'post_pk': self.post.pk, 'comment_pk': self.comment.pk})
        response = self.client.post(path=url, data={'reaction': self.reaction.emoji, 'comment': self.comment.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reaction_create_without_auth(self):
        self._logout()
        url = reverse('comment-reactions-list', kwargs={'post_pk': self.post.pk, 'comment_pk': self.comment.pk})
        response = self.client.post(path=url, data={'reaction': self.reaction.emoji, 'comment': self.comment.pk})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_reaction(self):
        url = reverse('comment-reactions-detail', kwargs={'post_pk': self.post.pk, 'comment_pk': self.comment.pk,
                                                          'pk': self.user_comment_reaction.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_reaction_as_anonymous(self):
        self._logout()
        url = reverse('post-reactions-detail', kwargs={'post_pk': self.post.pk, 'pk': self.user_post_reaction.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_reaction_as_admin(self):
        self._logout()
        mommy.make(User, username=self.second_username, password=make_password(self.password), is_staff=True)
        self.client.login(username=self.second_username, password=self.password)
        url = reverse('post-reactions-detail', kwargs={'post_pk': self.post.pk, 'pk': self.user_post_reaction.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _login(self):
        login = self.client.login(username=self.username, password=self.password)
        return login

    def _logout(self):
        self.client.logout()
