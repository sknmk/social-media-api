from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import test, status

from model_mommy import mommy
from timeline.posts.models import Post
from timeline.comments.models import Comment


class CommentViewTestCase(TestCase):
    username = 'test'
    password = '123456'

    def setUp(self):
        self.client = test.APIClient()
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self._login()
        self.post = mommy.make(Post, user=self.user, published_date=timezone.now())
        self.comment = mommy.make(Comment, user=self.user, post=self.post)

    def test_comment_instance(self):
        self.assertIsInstance(self.comment, Comment)

    def test_comment_list(self):
        url = reverse('comment-list', kwargs={'post_pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_create(self):
        url = reverse('comment-list', kwargs={'post_pk': self.post.pk})
        response = self.client.post(path=url, data={'text': 'Test Comment', 'post': self.post.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_create_without_auth(self):
        self._logout()
        url = reverse('comment-list', kwargs={'post_pk': self.post.pk})
        response = self.client.post(path=url, data={'text': 'Test Comment', 'post': self.post.pk})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_comment_detail(self):
        url = reverse('comment-detail', kwargs={'post_pk': self.post.pk, 'pk': self.comment.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse('comment-detail', kwargs={'post_pk': self.post.pk, 'pk': self.comment.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_comment_as_anonymous(self):
        self._logout()
        url = reverse('comment-detail', kwargs={'post_pk': self.post.pk, 'pk': self.comment.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_comment_as_admin(self):
        self.user.is_staff = True
        self.user.save()
        url = reverse('comment-detail', kwargs={'post_pk': self.post.pk, 'pk': self.comment.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _login(self):
        login = self.client.login(username=self.username, password=self.password)
        return login

    def _logout(self):
        self.client.logout()
