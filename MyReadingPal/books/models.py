from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    is_public = models.BooleanField()
    creator_id = models.IntegerField()
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    opinion = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

