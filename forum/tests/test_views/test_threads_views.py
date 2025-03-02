from datetime import datetime, timedelta

from django import urls
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class ThreadViewsetTest(APITestCase):

  def setUp(self):
    self.url = urls.reverse('threads-current-thread')
    self.client = APIClient()
    self.user = User.objects.create()

  def test_url_exists(self):
    self.assertEqual(self.url, '/api/threads/current-thread/')

  def test_view_returns_200(self):
    self.client.force_authenticate(self.user)
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)