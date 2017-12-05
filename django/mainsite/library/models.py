from django.db import models
from django.utils import timezone

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


class RentalStatus(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=True)
    user = models.CharField(max_length=25, null=True)
    timestamp = models.DateField(default=timezone.now())

    def __str__(self):
        return f'{self.user} {self.checked_in} {self.timestamp}'

