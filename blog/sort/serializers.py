from rest_framework import serializers
from .models import Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'