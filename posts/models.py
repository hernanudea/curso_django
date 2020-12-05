"""
Posts Models.
"""
# Djando
from django.db import models


class User(models.Model):
    """User model"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True)

    is_admin = models.BooleanField(default=False)

    create = models.DateTimeField(auto_now_add=True) # guarda la fecha de creación
    modified = models.DateTimeField(auto_now=True) # guarda la fecha en que se edito


