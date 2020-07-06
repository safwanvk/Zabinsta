from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
