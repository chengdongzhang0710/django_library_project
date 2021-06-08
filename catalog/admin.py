from django.contrib import admin

from .models import Author, Book

classes = [Author, Book]

for model in classes:
    admin.site.register(model)
