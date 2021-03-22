from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from .validators import validate_file_size

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug_field = str(self.title.lower()) + ' category'
        if not self.slug:
            self.slug = slugify(slug_field)
        return super().save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    document = models.FileField(
        upload_to='notes/', null=True, blank=True, validators=[validate_file_size])
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug_field = self.title + ' ' + str(self.author)
        if not self.slug:
            self.slug = slugify(slug_field)
        return super().save(*args, **kwargs)
