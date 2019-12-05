from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


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


class ModelPagoEfectivo(models.Model):
    time_create = models.DateTimeField(default=timezone.now, blank=True)
    object = models.CharField(max_length=250, default='', blank=True)
    create_data_time = models.IntegerField()
    expiration_date_time = models.IntegerField()
    orde_id = models.CharField(max_length=250, default='', blank=True, null=True)
    order_number = models.CharField(max_length=250, default='', blank=True, null=True)
    amount = models.FloatField(default=0.0, blank=True, null=True)
    payment_code = models.CharField(max_length=250, default='', blank=True, null=True)
    currency_code = models.CharField(max_length=250, default='', blank=True, null=True)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    state = models.CharField(max_length=250, default='', blank=True, null=True)
    total_fee = models.CharField(max_length=250, default='', blank=True, null=True)
    net_amount = models.CharField(max_length=250, default='', blank=True, null=True)
    fee_details = models.CharField(max_length=250, default='', blank=True, null=True)
    updated_at = models.CharField(max_length=250, default='', blank=True, null=True)
    paid_at = models.CharField(max_length=250, default='', blank=True, null=True)
    available_on = models.CharField(max_length=250, default='', blank=True, null=True)
    metadata = JSONField(blank=True, default=dict)
    firstname = models.CharField(max_length=400, default='', blank=True, null=True)
    lastname = models.CharField(max_length=400, default='', blank=True, null=True)
    phone = models.CharField(max_length=400, default='', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    data_payment = JSONField(blank=True, default=dict)

    def __str__(self):
        return '{} : {}'.format(self.email, self.state)


# Create your models here.
class ModelContact(models.Model):
    create = models.DateTimeField(default=timezone.now, blank=True)
    name = models.CharField(max_length=255, default='', blank=False)
    email = models.EmailField(max_length=255, blank=False)
    message = models.CharField(max_length=255, default='', blank=False)
    phone = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return '{}: {}: {}'.format(self.create, self.email, self.phone)
