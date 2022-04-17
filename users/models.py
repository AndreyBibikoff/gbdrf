from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

class TodoUser(AbstractUser):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email', unique=True)