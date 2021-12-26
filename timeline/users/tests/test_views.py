from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import test, status
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from model_mommy import mommy

from timeline.users.models import UserProfile, UserFollower


class UserTestMixin(TestCase):
    username = 'Lorem'
    password = '1881'

    def setUp(self):
        self.client = test.APIClient()
        self.user = mommy.make(User, username=self.username, password=make_password(self.password))
        self.user_profile = mommy.make(UserProfile, user=self.user, bio='Lorem ipsum dolor.', area='Istanbul Province',
                                       phone='905457426200')
        self._login()

    def _login(self):
        login = self.client.login(username=self.username, password=self.password)
        return login


class UserProfileTestCase(UserTestMixin):
    def test_get_user_profile(self):
        url = reverse('user-profile-detail', kwargs={'user_id': self.user.pk})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('bio'), 'Lorem ipsum dolor.')
        self.assertEqual(response.data.get('phone'), '905457426200')

    def test_update_user_profile(self):
        url = reverse('user-profile-detail', kwargs={'user_id': self.user.pk})
        data = {'bio': 'Updated bio.'}
        response = self.client.patch(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('bio'), 'Updated bio.')


class UserFollowerTestCase(UserTestMixin):
    def setUp(self):
        super(UserFollowerTestCase, self).setUp()
        self.an_user = mommy.make(User, username='{}2'.format(self.username), password=make_password(self.password))
        self.other_user = mommy.make(User, username='{}3'.format(self.username), password=make_password(self.password))
        self.follower = mommy.make(UserFollower, user=self.user, following=self.an_user)

    def test_create_user_follower(self):
        url = reverse('user-follower-list')
        data = {'following': self.other_user.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_fail_create_user_follower(self):
        url = reverse('user-follower-list')
        data = {'following': self.user.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_get_user_follower(self):
        url = reverse('user-follower-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_delete_user_follower(self):
        url = reverse('user-follower-detail', kwargs={'pk': self.follower.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
