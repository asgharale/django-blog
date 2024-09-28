from django.http import Http404 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter

class ArticleListView(generics.ListAPIView):
    queryset = Article.published.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
    filterset_class = ArticleFilter

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

class SearchArticleListView(APIView):
    def get(self, request, slug, fromat=None):
        pass
