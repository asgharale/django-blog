from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCommentListView

urlpatterns: list = [
    path("all/v1/", ArticleListView.as_view()),
    path("article/v1/<slug:slug>/", ArticleDetailView.as_view()),
    path("comments/v1/<slug:slug>/", ArticleCommentListView.as_view()),
]
