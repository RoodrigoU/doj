from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from mentor.views import python_mentor
urlpatterns = [
    path('', views.home, name='home'),
    path('python', csrf_exempt(python_mentor), name='python-mentor'),
    path('python-plan-mes-1-2', csrf_exempt(views.python_plan_mes_1_2), name='python-plan'),
    path('checkout', csrf_exempt(views.checkout), name='checkout'),
    path('checkout/success', csrf_exempt(views.checkoutSuccesss), name='checkout-successs'),
    path('webhook', csrf_exempt(views.webhook), name='webhook'),
]
