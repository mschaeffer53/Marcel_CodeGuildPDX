from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} {self.title} {self.body}'

class Comment(models.Model):
    user = models.ForeignKey(User)
    blogpost = models.ForeignKey(BlogPost)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} {self.body}'