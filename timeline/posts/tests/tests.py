from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND

from model_mommy import mommy
from timeline.posts.models import Post


class PostTests(TestCase):
    username = 'test'
    password = '123456'

    def setUp(self):
        self.client = APIClient()
        self.user = mommy.make(settings.AUTH_USER_MODEL, username=self.username)
        self.user.set_password(self.password)
        self.user.save()
        self._login()
        self.post = mommy.make(Post, user=self.user)

    def test_post_instance(self):
        self.assertIsInstance(self.post, Post)

    def test_post_list(self):
        url = reverse('post-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_post_create(self):
        url = reverse('post-list')
        response = self.client.post(path=url, data={"title": "Test Title", "slug": "test-slug", "text": "Test Content"})
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_post_create_without_auth(self):
        self._logout()
        url = reverse('post-list')
        response = self.client.post(path=url, data={"title": "Test Title", "slug": "test-slug", "text": "Test Content"})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_published_post_detail(self):
        self._publish_post()
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_unpublished_post_detail(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_post_admin_update(self):
        self.user.is_staff = True
        self.user.save()
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.put(path=url, data={"title": "updated title", "slug": "test-sl", "text": "upd. content"})
        self.assertEqual(response.status_code, HTTP_200_OK)

    def _publish_post(self):
        self.post.published_date = timezone.now() - timezone.timedelta(days=2)
        self.post.save()

    def _login(self):
        self.client.login(username=self.username, password=self.password)

    def _logout(self):
        self.client.logout()
