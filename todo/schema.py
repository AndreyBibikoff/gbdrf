import graphene
from graphene_django import DjangoObjectType
from .models import Project, Todo
from users.models import TodoUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'

class UsersType(DjangoObjectType):
    class Meta:
        model = TodoUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TodoType)
    all_users = graphene.List(UsersType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_all_users(root, info):
        return TodoUser.objects.all()


schema = graphene.Schema(query=Query)
