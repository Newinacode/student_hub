from django.contrib import admin
from .models import Question, Vote, QuestionView

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'description')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Vote)
admin.site.register(QuestionView)
