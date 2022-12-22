from django.contrib.auth.models import User
from django.db import models


class UserLikes(models.Model):
    liked_user = models.IntegerField()
    liker_user = models.IntegerField()