from datetime import datetime, timedelta

from django import urls
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from forum.tests.factories.thread_factory import ThreadFactory
from forum.views.thread_views import _get_current_thread


class ThreadViewsetTest(APITestCase):

  def setUp(self):
    self.url = urls.reverse('threads-current-thread')
    self.client = APIClient()
    self.user = User.objects.create()

  def test_url_exists(self):
    self.assertEqual(self.url, '/api/threads/current-thread/')

  def test_current_thread_returns_current_thread(self):
    now = datetime.now()
    three_days_ago = now - timedelta(days=3)
    three_days_from_now = now + timedelta(days=3)

    thread = ThreadFactory(
      valid_from=three_days_ago,
      valid_until = three_days_from_now
    )

    self.assertEqual(_get_current_thread(), thread)

  def test_view_returns_200(self):
    self.client.force_authenticate(self.user)
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)