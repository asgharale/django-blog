from django.urls import path
from .views import ListCategoryView, ListTagView

urlpatterns = [
    path("category/v1/all", ListCategoryView.as_view()),
    path("tag/v1/all", ListTagView.as_view()),
]