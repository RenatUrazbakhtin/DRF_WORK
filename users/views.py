from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserCreateSerializer


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer