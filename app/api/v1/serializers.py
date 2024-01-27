from rest_framework import serializers
from ...models import UserPasswordManager

class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPasswordManager
        fields = '__all__'

