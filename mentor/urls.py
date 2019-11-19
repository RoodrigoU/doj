from django.urls import path
from . import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('python-de-cero-a-ninja', views.taller_python, name='taller-python'),
    path('demo', views.demo, name='demo'),
    path('', views.mentor, name='mentor'),
]
