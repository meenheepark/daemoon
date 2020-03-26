from django.contrib import admin
from .models import Post, Category
from django import forms

admin.site.register(Post)
admin.site.register(Category)

