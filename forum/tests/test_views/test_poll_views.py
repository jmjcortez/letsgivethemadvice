from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from forum.models.user import User


class PollViewsetTest(APITestCase):

  def setUp(self):

    self.url = reverse('polls-current-poll')
    self.client = APIClient()
    self.user = User.objects.create()

  def test_url_exists(self):

    self.assertEqual(self.url, '/api/polls/current-poll/')

  def test_view_returns_200(self):

    self.client.force_authenticate(self.user)
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)