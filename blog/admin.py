from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Author, Post

admin.site.register(Post)
admin.site.register(Author)