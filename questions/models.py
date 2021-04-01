from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    vote = models.ManyToManyField(
        User, related_name='vote', default=None, blank=True)
    comments = GenericRelation(Comment)
    @property
    def views_count(self):
        return QuestionView.objects.filter(question=self.pk).count()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(
            f"{self.title} {self.author.id} {self.date_posted.strftime('%S')}")
        super(Question, self).save(*args, **kwargs)


class Vote(models.Model):
    question = models.ForeignKey(
        Question, related_name='questionid', on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid',
                             on_delete=models.CASCADE, default=None, blank=True)
    vote = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user) + '-> ' + str(self.question.title)


class QuestionView(models.Model):
    IPAddress = models.GenericIPAddressField(default='45.243.82.169')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.IPAddress} in {self.question.title} question'
