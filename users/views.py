from django.shortcuts import render

# Create your views here.
from rest_framework import mixins

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import TodoUser
from .serializers import UserModelSerializer


class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = UserModelSerializer
