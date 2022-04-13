from rest_framework import serializers

from rest_framework.serializers import ModelSerializer, StringRelatedField

from users.serializers import UserModelSerializer, SimpleUserModelSerializer
from .models import Project, Todo

class SimpleProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['name']


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


def get_project_name(obj):
    return obj.project.name


class TodoModelSerializer(ModelSerializer):
    user = UserModelSerializer()
    project = SimpleProjectSerializer()

    class Meta:
        model = Todo
        fields = '__all__'


class TodoModelSerializerBase(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
