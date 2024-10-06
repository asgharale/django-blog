from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCommentListView, CommentView

urlpatterns: list = [
    path("all/v1/", ArticleListView.as_view()),
    path("article/v1/<slug:slug>/", ArticleDetailView.as_view()),
    path("comments/v1/<slug:slug>/", ArticleCommentListView.as_view()),
    path("comment/v1/add/", CommentView.as_view()),
]
