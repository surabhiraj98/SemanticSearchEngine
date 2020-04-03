from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    religion = models.CharField(max_length=20)
    interest = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    education = models.CharField(max_length=50)