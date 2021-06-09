from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Book Image'
        verbose_name_plural = 'Book Images'

    def __str__(self):
        return self.book.title
