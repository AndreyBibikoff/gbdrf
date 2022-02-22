from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = UserModelSerializer
