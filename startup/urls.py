from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('python', csrf_exempt(views.python_startup), name='python-startup'),
    path('checkout', csrf_exempt(views.checkout), name='checkout'),
    path('checkout/success', csrf_exempt(views.checkoutSuccesss), name='checkout-successs'),
    path('webhook', csrf_exempt(views.webhook), name='webhook'),
]
