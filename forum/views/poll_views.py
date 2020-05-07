from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from forum.serializers.poll_serializers import PollSerializer
from forum.models.thread import Thread


class PollViewset(ViewSet):

  authentication_classes = ()
  permission_classes = ()

  @action(detail=False, url_path='current-poll')
  def current_poll(self, request):

    current_poll = None

    current_thread = Thread.objects.get_current_thread()

    if current_thread:
      current_poll = current_thread.poll

    serializer = PollSerializer(current_poll)

    return Response(status=status.HTTP_200_OK, data=serializer.data)
