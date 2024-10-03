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
        fields = [
            'username',
            'first_name',
            'last_name',
            'prof_picture',
            'bio',
            'phone_num',
            'birthdate',
            'pub_email',
            'tel_id',
            'github_id',
            'twitt_id',
            'youtube_id'
        ]
