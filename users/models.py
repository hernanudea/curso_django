"""Users models"""

# Djando
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """ Profile models
        Proxy model that extends the base data eith other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True) # requiere isntalar Pillow

    created = models.DateTimeField(auto_now_add=True) # pone la fecha de creación automaticamente
    modified = models.DateTimeField(auto_now=True) # actualiza la fecha de modificación automamente

    def __str__(self):
        """Return username"""
        return  self.user.username

