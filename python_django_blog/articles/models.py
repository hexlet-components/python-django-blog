from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    name = models.CharField('name', max_length=100, unique=True)
    description = models.TextField('description')
    created_at = models.DateTimeField('created date', default=timezone.now)

    def get_absolute_url(self):
        return reverse('articles:index')

    def __str__(self):
        return self.name
