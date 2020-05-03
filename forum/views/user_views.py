from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from forum.models.user import Voter
from forum.serializers.user_serializer import VoterListSerializer
from forum.view_models.user_view_models import VoterListViewModel


class VoterViewset(ViewSet):

    permission_classes = []
    authentication_classes = []

    def list(self, request, **kwargs):
        voters_list = Voter.objects.all()

        voters_list_vm = VoterListViewModel(voters_list=voters_list)
        serializer = VoterListSerializer(data=voters_list_vm.__dict__)

        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)