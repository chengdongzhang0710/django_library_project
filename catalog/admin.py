from django.contrib import admin

from .models import Author, Book, BookImage

classes = [Author, Book, BookImage]

for model in classes:
    admin.site.register(model)
