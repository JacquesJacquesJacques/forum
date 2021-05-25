from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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


class Priority(models.Model):
    label = models.CharField(max_length=40)

    def __str__(self):
        return self.label


class Post(models.Model):
    description = models.CharField(max_length=200)
    date_creation = models.DateField(default=timezone.now())
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    event = models.BooleanField(default=False)
    date_event = models.DateField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_creation']


class Comment(models.Model):
    date_creation = models.DateField(default=timezone.now())
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
