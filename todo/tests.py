from django.test import TestCase

# Create your tests here.

import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet, TodoModelViewSet
from users.views import UserModelViewSet
from .models import TodoUser, Todo, Project


class TestProjectViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/project/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {'name': 'superproject', 'link': 'https://git.local/fdskjf'},
                               format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestTodoViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        project = mixer.blend(Project)
        client = APIClient()
        response = client.put(f'/api/project/{project.id}/', {'name': 'newname', 'link': 'https://git.local/newlink'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        project = mixer.blend(Project)
        user = TodoUser.objects.create_superuser('admin', 'admin@admin.local', 'admin')
        todo = Todo.objects.create(text='Что это за проект?', project=project, user=user)
        print(user.uuid_id)
        self.client.login(username='admin', password='admin')
        response = self.client.put(f'/api/todo/{todo.id}/', {'text': 'Что это за проект вообще?', 'project': project.id,
                                                             'user': todo.user.uuid_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = Todo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'Что это за проект вообще?')
