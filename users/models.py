from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_id = models.CharField(max_length=10)


# Create your models here.
