from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)
    is_final = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Note(models.Model):
    text = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
