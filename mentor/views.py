from django.shortcuts import render
import requests
from shop.models import ModelIps


TK_DETECT_COUNTRY = 'dfc4899fc100cb167072406ee001ac81'


CURRENCY_CONVERT = {
    'PE': {'mount': '159', 'simbol': 'S/ '},
    'CO': {'mount': '163,000', 'simbol': '$ '},
    'EC': {'mount': '1,200,000', 'simbol': '$ '},
    'MX': {'mount': '917', 'simbol': '$ '},
    'SV': {'mount': '412,000', 'simbol': '$ '},
    'ES': {'mount': '45', 'simbol': '€'},
    'AR': {'mount': '2,850', 'simbol': '$'},
    'CL': {'mount': '37,500', 'simbol': '$'},
    'BO': {'mount': '327', 'simbol': '$'},
    'VE': {'mount': '470', 'simbol': '$'},
}

def get_info_ip(ip):
    try:
        uri = 'http://api.ipstack.com/{}?access_key={}'.format(ip, TK_DETECT_COUNTRY)
        r = requests.get(uri, verify=False, timeout=5)
        if 200 <= r.status_code <= 300:
            return r.json()
        else:
            print('error')
            return False
    except:
        return False


def get_currency(country_code):
    mount, simbol = 0, ''
    if CURRENCY_CONVERT.get(country_code, False):
        mount = CURRENCY_CONVERT[country_code]['mount']
        simbol = CURRENCY_CONVERT[country_code]['simbol']
    else:
        mount = '49'
        simbol = '$'
    return mount, simbol


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def mentor(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = 'api'
    else:
        uri_whatsapp = 'web'
    return render(request, 'base_mentor.html', {'uri_whatsapp': uri_whatsapp})


def demo(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."

    return render(request, 'demo.html', {'uri_whatsapp': uri_whatsapp})


def taller_python(request):
    mobile = False
    mount, simbol, country_flag = '', '', ''
    client_ip = visitor_ip_address(request)
    if '127.0.0.1' in client_ip or '192.168.1.' in client_ip:
        client_ip = '200.106.89.166' #peru
    id_, created = ModelIps.objects.get_or_create(
            ip=client_ip,
    )
    country_code = id_.country_code
    country_code = False
    if country_code:
        country_flag = id_.country_flag
        country_flag = country_flag.replace('http://', 'https://')
        mount, simbol = get_currency(country_code)
    else:
        info_ip = get_info_ip(client_ip)
        country_code = info_ip['country_code']
        country_name = info_ip['country_name']
        country_flag = info_ip['location']['country_flag']
        if country_flag:
            country_flag = country_flag.replace('http://', 'https://')
        calling_code = info_ip['location']['calling_code']
        id_.country_code = country_code
        id_.country_name = country_name
        id_.calling_code = calling_code
        id_.save()
        mount, simbol = get_currency(country_code)

    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = "api"
        return render(request, 'taller_python_mobile.html', {'uri_whatsapp': uri_whatsapp,
         'uri_whatsapp': uri_whatsapp,
           'mount': mount,
            'simbol': simbol,
            'country_flag': country_code.lower()})
    else:
        uri_whatsapp = "web"
        return render(request, 'taller_python.html', {'uri_whatsapp': uri_whatsapp,
         'uri_whatsapp': uri_whatsapp,
           'mount': mount,
            'simbol': simbol,
            'country_flag': country_code.lower()})
