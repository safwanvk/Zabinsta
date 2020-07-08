from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    caption = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('insta:post_detail', kwargs={"id": self.id})

    def __str__(self):
        return self.caption

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.commenter)
