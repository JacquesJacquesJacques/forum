from django.contrib.auth.models import User
from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ManyToManyField(Community)

    def __str__(self):
        return "Profile of {0}".format(self.user.username)
