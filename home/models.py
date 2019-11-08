from django.db import models


class ModelContact(models.Model):
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, blank=False)
    message = models.CharField(max_length=255, default='')

    def __str__(self):
        return '{}: {}'.format(self.email, self.name)
