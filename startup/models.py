from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class ModelPayment(models.Model):
    time_create = models.DateTimeField(default=timezone.now, blank=True)
    status_object = models.CharField(max_length=300, default='', blank=True)
    amount = models.FloatField(default=0.0, blank=True)
    charge_id = models.CharField(max_length=300, default='', blank=True)
    type = models.CharField(max_length=300, default='', blank=True)
    code = models.CharField(max_length=300, default='', blank=True)
    reference_code = models.CharField(max_length=300, default='', blank=True)
    authorization_code = models.CharField(max_length=300, default='', blank=True)
    merchant_message = models.CharField(max_length=300, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    data_payment = JSONField(blank=True, default=dict)
    name = models.CharField(max_length=400, default='', blank=True)
    lastname = models.CharField(max_length=400, default='', blank=True)
    phone = models.CharField(max_length=400, default='', blank=True)

    def __str__(self):
        return '{} : {}: {}'.format(self.email, self.type, self.phone)


# Create your models here.
class ModelContact(models.Model):
    create = models.DateTimeField(default=timezone.now, blank=True)
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, blank=False)
    message = models.CharField(max_length=255, default='', blank=False)
    phone = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return '{}: {}: {}'.format(self.create, self.email, self.phone)
