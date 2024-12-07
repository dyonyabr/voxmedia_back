from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import date
from datetime import time


class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default="da")
    avatar = models.ImageField(default="user/default_avatar.png", upload_to="users")
    creation_time = models.TimeField(default=datetime.now().time(), blank=True)
    creation_date = models.DateField(default=date.today(), blank=True)

    def __str__(self) -> str:
        return str(self.id) + ". " + self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")
    content = models.JSONField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    upload_time = models.TimeField(default=datetime.now().time(), blank=True)
    upload_date = models.DateField(default=date.today(), blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    upload_time = models.TimeField(default=datetime.now().time(), blank=True)
    upload_date = models.DateField(default=date.today(), blank=True)

    def __str__(self) -> str:
        return str(self.id) + ". " + self.user.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
