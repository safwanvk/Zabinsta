from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def published(self):
        created_dates = self.created_date.replace(tzinfo=None)
        Now = datetime.now()
        Now = Now.replace(microsecond=0)
        time_difference = Now - created_dates
        if time_difference.days == 0:
            if int(time_difference.seconds / 3600) == 0:
                self.published_date = str(int(time_difference.seconds / 60)) + " MINUTES AGO"
            else:
                self.published_date = str(int(time_difference.seconds / 3600)) + " HOURS AGO"
        else:
            self.published_date = str(int(time_difference.days)) + " DAYS AGO"
        self.save()
        return self.published_date
