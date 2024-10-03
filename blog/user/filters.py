import django_filters
from .models import CUser

class CUserFilter(django_filters.FilterSet):
    class Meta:
        model = CUser
        fields = {
            'username': ['exact', 'icontains'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'pub_email': ['exact', 'icontains'],
        }
