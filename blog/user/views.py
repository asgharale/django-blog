from django.http import Http404 

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import CUser
from .serializers import CUserSerializer, ListCUserSerializer
from .filters import CUserFilter


class ListUserView(generics.ListAPIView):
    permission_classes: list = [AllowAny]
    queryset = CUser.objects.all()
    filter_backends: list = [DjangoFilterBackend]
    serializer_class = ListCUserSerializer
    filterset_class = CUserFilter

class UserDetailView(APIView):
    def get_object(self, username):
        try:
            return CUser.objects.get(username=username)
        except CUser.DoesNotExist:
            return Http404
    
    def get(self, request, username, fromat=None) -> Response:
        user = self.get_object(username)
        serializer = CUserSerializer(user)
        return Response(serializer.data)

