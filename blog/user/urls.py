from django.urls import path
from .views import ListUserView, UserDetailView

urlpatterns = [
    path("all/v1/", ListUserView.as_view()),
    path("user/<slug:username>", UserDetailView.as_view()),
]
