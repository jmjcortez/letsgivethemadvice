from datetime import datetime, timedelta

from django.test import TestCase

from forum.tests.factories.thread_factory import ThreadFactory
from forum.models.thread import Thread

class ThreadManagerTest(TestCase):

  def test_current_thread_returns_current_thread(self):
    now = datetime.now()
    three_days_ago = now - timedelta(days=3)
    three_days_from_now = now + timedelta(days=3)

    thread = ThreadFactory(
      valid_from=three_days_ago,
      valid_until=three_days_from_now
    )

    self.assertEqual(Thread.objects.get_current_thread(), thread)