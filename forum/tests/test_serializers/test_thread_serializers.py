from django.test import TestCase

from forum.serializers.thread_serializers import ThreadSerializer
from forum.tests.factories.thread_factory import ThreadFactory


class ThreadSerializerTest(TestCase):

  def setUp(self):
    serializer = ThreadSerializer

    self.maxDiff = None

  def test_deserializes_correct_fields(self):

    thread = ThreadFactory()

    thread_serializer_data = ThreadSerializer(thread).data

    self.assertEqual(
      set(thread_serializer_data.keys()),
      {
        'title', 'body', 'date_posted', 'date_created', 'aftermath', 'valid_from', 'valid_until',
      }
    )
