from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Feedback(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
