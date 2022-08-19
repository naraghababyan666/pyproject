# Create your views here.

import json
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .authentication import *

from user.serializers import UserSerializer
from .models import User


class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password!')

        token = create_token(user.id)

        return Response({
            "token": token
        })


class RefreshToken(APIView):
    def post(self, request):
        token = refresh_token(request.data['token'])
        return Response({
            'a': token
        })
