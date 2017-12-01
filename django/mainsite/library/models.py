from django.db import models
import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=99)
    pub_date = models.DateField()
    author = models.ManyToOneRel()

    def __str__(self):
        return f'{self.title} {self.pub_date} {self.author}'


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

