from django.http import Http404 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from .models import CUser
from .serializers import CUserSerializer

class UserListView(APIView):
    def get(self, request, fromat=None):
        users = CUser.admins.all()
        serializer = CUserSerializer(users, many=True)
        return Response()
