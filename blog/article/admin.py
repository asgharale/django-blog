from django.contrib import admin
from .models import Article, BlogComment

admin.site.register(Article)
admin.site.register(BlogComment)