from django.urls import path
from . import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('/python-de-cero-a-ninja', views.taller_python, name='mentor'),
    path('', views.mentor, name='mentor'),
]
