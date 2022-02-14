from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=60)
#     join_date = models.DateTimeField(auto_now_add=True)