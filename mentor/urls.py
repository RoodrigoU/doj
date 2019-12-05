from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path('python', csrf_exempt(views.python_mentor), name='python'),
    re_path('(?P<name_url>[a-zA-Z0-9-]+)', views.certificate, name='certificate'),
]
