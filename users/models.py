from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=80)
    age = models.IntegerField()

