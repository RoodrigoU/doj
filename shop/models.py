from django.db import models
from django.utils import timezone


# Create your models here.
class ModelIps(models.Model):
    time_create = models.DateTimeField(default=timezone.now, blank=True)
    ip = models.CharField(max_length=250, default='', blank=True)
    country_code = models.CharField(max_length=250, default='', blank=True)
    country_name = models.CharField(max_length=250, default='', blank=True)
    country_flag = models.CharField(max_length=250, default='', blank=True)
    calling_code = models.CharField(max_length=250, default='', blank=True)
    currency = models.CharField(max_length=250, default='', blank=True)
    mount = models.FloatField(default=0.0)

    def __str__(self):
        return '{}:{}'.format(self.ip, self.country_code)
