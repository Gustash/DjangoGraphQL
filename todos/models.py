from django.db import models

# Create your models here.
class Author(models.Model):
    __name__ = "author"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Todo(models.Model):
    __name__ = "todo"

    text = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='todos'
    )