from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from questions.models import Question
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.user) + ' commented on ' + str(self.question)
