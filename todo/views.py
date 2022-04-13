from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer, TodoModelSerializerBase
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, TodoProjectFilter


class ProjectLimitOfSetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOfSetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOfSetPagination
    filterset_class = ProjectFilter


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOfSetPagination
    filterset_class = TodoProjectFilter

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoModelSerializer
        return TodoModelSerializerBase
