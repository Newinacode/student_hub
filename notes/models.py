from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    document = models.FileField(upload_to='notes/')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
