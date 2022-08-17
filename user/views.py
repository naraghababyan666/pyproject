from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from user.serializers import UserSerializer
from rest_framework.views import APIView


class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def get(self, request):
        return