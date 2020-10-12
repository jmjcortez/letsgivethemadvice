from rest_framework import serializers

from forum.models.thread import Thread
from forum.serializers.poll_serializers import PollSerializer, ChoiceSerializer


class ThreadSerializer(serializers.ModelSerializer):

  class Meta:
    model = Thread
    fields = (
      'title', 'body', 'date_posted', 'date_created', 'aftermath', 'valid_from',
      'valid_until',
    )
