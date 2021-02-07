from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title} {self.author.id} {self.date_posted.strftime('%S')}")
        super(Question, self).save(*args, **kwargs)
