from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
]
