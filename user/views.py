# Create your views here.
import datetime
import json
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

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

        payload = {
            'id': user.id,
            'expiration': str(datetime.datetime.utcnow() + datetime.timedelta(minutes=60)),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            "token": token,
        })

class RefreshToken(APIView):
    def post(self, request):
        data = jwt.decode(request.data['token'], 'secret', algorithms=['HS256'])

        return Response({
            'a': data
        })
