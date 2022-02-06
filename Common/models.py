from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()
    number = models.CharField(max_length=15)
