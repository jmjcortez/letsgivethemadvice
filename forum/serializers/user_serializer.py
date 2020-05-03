from rest_framework import serializers

from forum.models.user import Voter


class VoterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    times_voted = serializers.IntegerField()
    

class VoterListSerializer(serializers.Serializer):
  voters = VoterSerializer(many=True)