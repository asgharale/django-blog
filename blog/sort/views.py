from django.http import Http404 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer


class ListCategoryView(APIView):
    permission_classes: list = [AllowAny]

    def get(self, request, fromat=None) -> Response:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ListTagView(APIView):
    permission_classes: list = [AllowAny]

    def get(self, request, fromat=None) -> Response:
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)