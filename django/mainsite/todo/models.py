from django.db import models

# Create your models here.

class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self):
        return self.todo_text

