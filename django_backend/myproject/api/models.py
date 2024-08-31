from django.db import models

# Create your models here.

# api/models.py
from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    roles = models.JSONField(default=dict)  # For storing roles as a JSON
    refresh_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
