from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    answer = models.BooleanField(default=False)
    

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

 