from django.urls import path

from .views import UserDetailAPI, RegisterUserAPIView, CustomLoginView

urlpatterns = [
    path("get-details/", UserDetailAPI.as_view()),
    path('get-token/', CustomLoginView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    ]