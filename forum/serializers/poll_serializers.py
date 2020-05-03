from rest_framework import serializers

from forum.models.poll import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):

  class Meta:
    model = Choice
    fields = (
      'text', 'num_of_votes',
    )


class PollSerializer(serializers.ModelSerializer):

  poll_choices = ChoiceSerializer(many=True)

  class Meta:
    model = Poll
    fields = (
      'question', 'poll_choices'
    )