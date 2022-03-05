from django.db import models

from users.models import TodoUser


class Project(models.Model):
    name = models.CharField(verbose_name='имя', max_length=128)
    link = models.CharField(verbose_name='ссылка', max_length=512)
    users = models.ManyToManyField(TodoUser)


class Todo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='текст заметки')
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлено', auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(TodoUser, on_delete=models.PROTECT)