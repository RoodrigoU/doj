from shop.models import ModelIps
import requests

TK_DETECT_COUNTRY = 'dfc4899fc100cb167072406ee001ac81'

CURRENCY_CONVERT = {
    'PE': {'mount': '120', 'simbol': 'S/. '},
    'CO': {'mount': '163,000', 'simbol': '$ '},
    'EC': {'mount': '1,200,000', 'simbol': '$ '},
    'MX': {'mount': '689', 'simbol': '$ '},
    'SV': {'mount': '412,000', 'simbol': '$ '},
    'ES': {'mount': '44', 'simbol': '€'},
    'AR': {'mount': '2,850', 'simbol': '$'},
    'CL': {'mount': '37,500', 'simbol': '$'},
    'BO': {'mount': '327', 'simbol': '$'},
    'PY': {'mount': '303,270', 'simbol': '$'},
    'UY': {'mount': '1,775', 'simbol': '$'},
    'NI': {'mount': '1,595', 'simbol': '$'},
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
    except Exception as e:
        print(ex)
        return False


def get_currency(country_code):
    mount, simbol = 0, ''
    if CURRENCY_CONVERT.get(country_code, False):
        mount = CURRENCY_CONVERT[country_code]['mount']
        simbol = CURRENCY_CONVERT[country_code]['simbol']
    else:
        mount = '47'
        simbol = '$'
    return mount, simbol


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_mount_for_county(request):
    mount, simbol, country_code = '', '', ''
    client_ip = visitor_ip_address(request)
    if '127.0.0.1' in client_ip or '192.168.1.' in client_ip:
        client_ip = '200.106.89.166' #peru
    id_, created = ModelIps.objects.get_or_create(
            ip=client_ip,
    )
    country_code = id_.country_code
    # client_ip = '148.217.94.54'
    # country_code = False
    if country_code:
        mount, simbol = get_currency(country_code)
    else:
        info_ip = get_info_ip(client_ip)
        if not info_ip:
            return mount, simbol, country_code
        country_code = info_ip['country_code']
        country_name = info_ip['country_name']
        calling_code = info_ip['location']['calling_code']
        id_.country_code = country_code
        id_.country_name = country_name
        id_.calling_code = calling_code
        id_.save()
        mount, simbol = get_currency(country_code)
    return mount, simbol, country_code
