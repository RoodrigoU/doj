from django.contrib import admin
from .models import ModelContact, ModelPayment
# Register your models here.
admin.site.register(ModelContact)
admin.site.register(ModelPayment)
