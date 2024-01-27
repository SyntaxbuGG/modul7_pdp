from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from .serializers import PasswordSerializer
from ...models import UserPasswordManager


class PasswordViewSet(viewsets.ModelViewSet):
    queryset = UserPasswordManager.objects.all()
    serializer_class = PasswordSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['^username']
    filterset_fields = ['application_type']





