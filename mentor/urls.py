from django.urls import path, re_path
from . import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('python-de-cero-a-ninja', views.taller_python, name='taller-python'),
    path('flujo', views.demo, name='flujo'),
    re_path('(?P<name_url>[a-zA-Z0-9-]+)', views.certificate, name='certificate'),

]
