from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import test, status

from model_mommy import mommy
from timeline.posts.models import Post


class PostViewTestCase(TestCase):
    username = 'test'
    second_username = 'second_test_user'
    password = '123456'

    def setUp(self):
        self.client = test.APIClient()
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self._login()
        self.post = mommy.make(Post, user=self.user)
        self._publish_post()

    def test_post_instance(self):
        self.assertIsInstance(self.post, Post)

    def test_post_list(self):
        url = reverse('post-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        url = reverse('post-list')
        response = self.client.post(path=url, data={'title': 'Test Title', 'slug': 'test-slug', 'text': 'Test Content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_edit_own_object(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.put(path=url,
                                   data={'title': 'try update', 'slug': 'this-post', 'text': 'can you?'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_edit_or_delete_another_users_object(self):
        self._logout()
        mommy.make(User, username=self.second_username, password=make_password(self.password))
        self.client.login(username=self.second_username, password=self.password)
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.put(path=url, data={'title': 'try update', 'slug': 'this-post', 'text': 'can you?'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_edit_or_delete_as_anonymous(self):
        self._logout()
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.put(path=url, data={'title': 'try update', 'slug': 'this-post', 'text': 'can you?'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_without_auth(self):
        self._logout()
        url = reverse('post-list')
        response = self.client.post(path=url, data={'title': 'Test Title', 'slug': 'test-slug', 'text': 'Test Content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_detail(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unpublished_post_detail(self):
        self._close_post()
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_and_delete_post_as_admin(self):
        self._logout()
        mommy.make(User, username=self.second_username, password=make_password(self.password), is_staff=True)
        self.client.login(username=self.second_username, password=self.password)
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.put(path=url, data={'title': 'updated title', 'slug': 'test-sl', 'text': 'upd. content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_filters(self):
        url = reverse('post-list') + f'?search={self.post.title}'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['title'], self.post.title)

        posts = Post.objects.filter(user=self.user)
        self.assertEqual(posts.count(), 1)

        url = reverse('post-list') + f'?user={self.post.user.id}'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['title'], self.post.title)

    def _publish_post(self):
        self.post.published_date = timezone.now() - timezone.timedelta(days=2)
        self.post.save()

    def _close_post(self):
        self.post.published_date = None
        self.post.save()

    def _login(self):
        login = self.client.login(username=self.username, password=self.password)
        return login

    def _logout(self):
        self.client.logout()
