from django.db import models
from django.conf import settings

from catalog.models import Book


class Review(models.Model):
    RATING_CHOICES = ((5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    value = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')

    class Meta:
        verbose_name = 'Book Review'
        verbose_name_plural = 'Book Reviews'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.book.title}/{self.user.username} - {self.value}'
