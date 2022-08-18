from django.urls import path
from .views import Register, Login, RefreshToken

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('refresh-token', RefreshToken.as_view())
]
