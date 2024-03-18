from django.contrib import admin
from .models import Author, Post


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email']



admin.site.register(Post)
