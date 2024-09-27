# django
from django.http import Http404 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer


class ArticleListView(APIView):
    def get(self, request, fromat=None):
        articles = Article.published.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    def get_object(self, slug):
        try:
            return Article.published.get(address=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug, fromat=None):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
