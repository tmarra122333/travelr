from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    join_date = models.DateTimeField(auto_now_add=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

class Guide(models.Model):
    title = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    category = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="guides")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")




