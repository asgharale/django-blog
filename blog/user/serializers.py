from rest_framework import serializers
from .models import CUser

class ListCUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'prof_picture',
        ]

class CUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = '__all__'