import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            'title': ['exact', 'icontains'],
            'category': ['exact'],
            'author': ['exact'],
            # 'price': ['lt', 'gt'],           # امکان فیلتر بر اساس قیمت (کمتر از یا بیشتر از)
        }
