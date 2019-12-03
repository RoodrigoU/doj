from django.shortcuts import render
import requests
from .models import ModelAlumno
from shop.models import ModelIps
from modules.detect_currency_country import *


def certificate(request, name_url):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = 'api'
    else:
        uri_whatsapp = 'web'

    obj = ModelAlumno.objects.filter(url_alumno=name_url)
    if obj:
        obj = obj[0]
        name = obj.nombre
        last_name = obj.apellido
        name_taller = obj.taller_name
        file_certificate = obj.file_certificate
    else:
        return render(request, 'base.html')

    return render(request, 'certificate.html',
            {
                'uri_whatsapp': uri_whatsapp,
                'name': name,
                'last_name': last_name,
                'name_taller': name_taller,
                'file_certificate': file_certificate
            })
