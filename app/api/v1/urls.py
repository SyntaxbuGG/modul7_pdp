from rest_framework import routers
from django.urls import path,include
from .views import PasswordViewSet

router = routers.DefaultRouter()

router.register(r'questions', PasswordViewSet)

urlpatterns = router.urls


