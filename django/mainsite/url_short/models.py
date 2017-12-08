from django.db import models


# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=200)
    short = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.url} {self.short}'
