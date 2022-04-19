from django.shortcuts import render

# Create your views here.
from rest_framework import mixins

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import TodoUser
from .serializers import UserModelSerializerV1, UserModelSerializerV2


class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = UserModelSerializerV1

    def get_serializer_class(self):
        if self.request.version == '2':
            return UserModelSerializerV2
        return UserModelSerializerV1
