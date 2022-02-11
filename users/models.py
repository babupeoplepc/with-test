from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    student_name = models.CharField(max_length=10)
    student_gender = models.CharField(max_length=2)
    student_email = models.CharField(max_length=100)
    student_phone_number = models.CharField(max_length=20)
    student_birth_year = models.IntegerField(default=0)
    student_birth_month = models.IntegerField(default=0)
    student_birth_day = models.IntegerField(default=0)
    student_home_address = models.CharField(max_length=100)
    student_job = models.CharField(max_length=20, blank=True)
    student_visit = models.CharField(max_length=20, blank=True)
    student_visit_example = models.TextField(blank=True)
    student_comment = models.TextField(blank=True)
    student_lesson_comment = models.TextField(blank=True)
    student_push_stop = models.BooleanField(default=False)
    





