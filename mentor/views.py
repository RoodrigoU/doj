from django.shortcuts import render
import requests
from .models import ModelAlumno
from modules.detect_currency_country import *


def python_mentor(request):
    mobile = False
    mount, simbol, country_code = get_mount_for_county(request)
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = "api"
        return render(request, 'python_mentor.html', {'uri_whatsapp': uri_whatsapp,
         'uri_whatsapp': uri_whatsapp,
           'mount': mount,
            'simbol': simbol,
            'country_flag': country_code.lower()})
    else:
        uri_whatsapp = "web"
        return render(request, 'python_mentor.html', {'uri_whatsapp': uri_whatsapp,
         'uri_whatsapp': uri_whatsapp,
           'mount': mount,
            'simbol': simbol,
            'country_flag': country_code.lower()})  #country_code.lower()


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
