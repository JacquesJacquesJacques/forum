from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Community(models.Model):      # Represents a group of user
    name = models.CharField(max_length=100)     # The title of the community
    followers = models.ManyToManyField(User)    # Every user who follows the community

    def __str__(self):
        return self.name


class Priority(models.Model):       # Represents the priority level of a post (urgent, etc...)
    label = models.CharField(max_length=40)

    def __str__(self):
        return self.label


class Post(models.Model):       # Represents the content of the site: post exposing facts, news, opinions, ...
    title = models.CharField(max_length=200)                            # title of what is written
    date_creation = models.DateField(default=timezone.now())            # the date it was written
    community = models.ForeignKey(Community, on_delete=models.CASCADE)  # the community it is part of
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)    # the level of priority
    event = models.BooleanField(default=False)                          # is it an event or not
    date_event = models.DateField(null=True, blank=True)                # if yes, when is it ?
    author = models.ForeignKey(User, on_delete=models.CASCADE)          # the user who wrote it
    description = models.TextField()                                    # the content of the post

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_creation']


class Comment(models.Model):    # Represents post comments
    date_creation = models.DateField(default=timezone.now())    # when it was written
    content = models.TextField()                                # what it says
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # the user who wrote it
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # the post it refers to
