from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)

