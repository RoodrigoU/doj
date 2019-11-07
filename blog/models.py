from django.db import models
from django.utils import timezone


class ModelBlog(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=255, default='')
    body = models.TextField()
    url_image = models.CharField(max_length=255, default='')
    resume = models.CharField(max_length=255, default='')

    def __str__(self):
        return '{} - {}'.format(self.author, self.created_date)


class ModelContact(models.Model):
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, blank=False)
    message = models.CharField(max_length=255, default='')

    def __str__(self):
        self.email
