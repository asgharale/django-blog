from django.contrib import admin
from .models import Article, Comment
from django_jalali.admin.filters import JDateFieldListFilter

class ArticleAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_at', JDateFieldListFilter), 
    )

class CommentAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_at', JDateFieldListFilter),
    )
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
