from django.urls import path
from .views import ListUserView, UserView

urlpatterns = [
    path("all/v1/", ListUserView.as_view()),
    path("user/<slug:username>", UserView.as_view()),
]
