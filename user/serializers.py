from django.utils import timezone
from rest_framework import serializers
from rest_framework.response import Response

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'email', 'password', 'created', 'updated']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
