from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from forum.serializers.thread_serializers import ThreadSerializer
from forum.models.thread import Thread


class ThreadViewset(ViewSet):

  # No auth needed, only voting needs auth
  authentication_classes = ()
  permission_classes = ()

  def list(self, request):
    threads = list(Thread.objects.all())

    serializer = ThreadSerializer(threads, many=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)

  @action(detail=False, url_path='current-thread')
  def current_thread(self, request):

    current_thread = Thread.objects.get_current_thread()

    serializer = ThreadSerializer(current_thread)

    return Response(status=status.HTTP_200_OK, data=serializer.data)
    pass