from django.urls import path
from .views import ArticleListView, ArticleDetailView, SearchArticleListView

urlpatterns = [
    path("all/v1/", ArticleListView.as_view()),
    path("article/v1/<slug:slug>/", ArticleDetailView.as_view()),
    path("search/v1/", SearchArticleListView.as_view()),
]