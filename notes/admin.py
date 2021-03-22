from django.contrib import admin
from .models import Note, Category

# Register your models here.


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title', 'author',),
    }
