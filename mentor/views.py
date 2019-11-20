from django.shortcuts import render
import requests

TK_DETECT_COUNTRY = 'dfc4899fc100cb167072406ee001ac81'


def get_info_ip(ip):
    try:
        # uri = 'http://api.ipstack.com/{}?access_key={}&fields=country_code'.format(ip, TOKEN)
        uri = 'http://api.ipstack.com/{}?access_key={}'.format(ip, TK_DETECT_COUNTRY)
        r = requests.get(uri, verify=False, timeout=5)
        if 200 <= r.status_code <= 300:
            print(r.json())
            return r.json()
        else:
            print('error')
            return False
    except:
        return False


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
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."

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
    client_ip = visitor_ip_address(request)
    if '127.0.0.1' in client_ip or '192.168.1.' in client_ip:
        client_ip = '200.106.89.166' #peru
    info_ip = get_info_ip(client_ip)
    with open('/tmp/ip.txt', 'w') as f:
        f.write(client_ip)
        f.write(str(info_ip))

    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_reserva = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%2C%20quisiera%20reservar%20la%20prueba%20gratuita%20del%20Taller%20Python."
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
        uri_buy = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20comprar%20el%20Taller%20de%20Python."
        return render(request, 'taller_python_mobile.html', {'uri_whatsapp': uri_whatsapp, 'uri_reserva': uri_reserva, 'uri_buy':uri_buy})
    else:
        uri_reserva = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%2C%20quisiera%20reservar%20la%20prueba%20gratuita%20del%20Taller%20Python."
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
        uri_buy = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20comprar%20el%20Taller%20de%20Python."
        return render(request, 'taller_python.html', {'uri_whatsapp': uri_whatsapp, 'uri_reserva': uri_reserva, 'uri_buy':uri_buy})
