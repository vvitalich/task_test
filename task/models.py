from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
