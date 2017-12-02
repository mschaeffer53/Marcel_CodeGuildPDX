from django.db import models
import datetime
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=99)
    pub_date = models.DateField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return f'{self.title} {self.pub_date} {self.author}'



