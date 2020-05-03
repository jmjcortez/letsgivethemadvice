from datetime import datetime

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from forum.serializers.thread_serializers import ThreadSerializer
from forum.models.thread import Thread


class ThreadViewset(ViewSet):

  # No auth needed, only voting needs auth

  def list(self, request):
    threads = list(Thread.objects.all())

    serializer = ThreadSerializer(threads, many=True)

    return Response(status=status.HTTP_200_OK, data=serializer.data)

  @action(detail=False, url_path='current-thread')
  def current_thread(self, request):
    serializer = ThreadSerializer(_get_current_thread())

    return Response(status=status.HTTP_200_OK, data=serializer.data)

def _get_current_thread():
  now = datetime.now()

  return Thread.objects.filter(valid_from__lte=now, valid_until__gte=now).first()
