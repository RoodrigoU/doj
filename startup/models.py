from django.db import models
from django.utils import timezone


# Create your models here.
class ModelContact(models.Model):
    create = models.DateTimeField(default=timezone.now, blank=True)
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, blank=False)
    message = models.CharField(max_length=255, default='', blank=False)
    phone = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return '{}: {}: {}'.format(self.create, self.email, self.phone)
