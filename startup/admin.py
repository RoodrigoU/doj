from django.contrib import admin
from .models import ModelContact, ModelPayment, ModelPagoEfectivo
# Register your models here.
admin.site.register(ModelContact)
admin.site.register(ModelPayment)
admin.site.register(ModelPagoEfectivo)
