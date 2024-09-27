from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'article',
            'email',
            'full_name',
            'message'
        ]