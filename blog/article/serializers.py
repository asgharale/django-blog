from rest_framework import serializers
from .models import Article, Comment
from sort.serializers import CategorySerializer, TagSerializer
from user.serializers import ListCUserSerializer

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    tag = TagSerializer(many=True)
    author = ListCUserSerializer

    class Meta:
        model = Article
        fields: list = [
            'title',
            'address',
            'meta',
            'thumbnail',
            'category',
            'tags',
            'body',
            'author',
            'read_time',
            'created_at',
            'open_conv',
            'likes_count',
            'views_count'
        ]


class ListArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author = ListCUserSerializer


    class Meta:
        model = Article
        fields: list = [
            'title',
            'address',
            'meta',
            'thumbnail',
            'category',
            'author',
            'created_at',
            'likes_count',
            'views_count'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields: list = [
            'full_name',
            'message'
        ]
