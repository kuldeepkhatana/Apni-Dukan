from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    """This is Model is used for user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.user)

