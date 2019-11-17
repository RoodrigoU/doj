from django.shortcuts import render

# Create your views here.
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


def taller_python(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_reserva = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%2C%20quisiera%20reservar%20la%20prueba%20gratuita%20del%20Taller%20Python."
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
        uri_buy = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20comprar%20el%20Taller%20de%20Python."
    else:
        uri_reserva = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%2C%20quisiera%20reservar%20la%20prueba%20gratuita%20del%20Taller%20Python."
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20Taller%20Python."
        uri_buy = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20quisiera%20comprar%20el%20Taller%20de%20Python."

    return render(request, 'taller_python.html', {'uri_whatsapp': uri_whatsapp, 'uri_reserva': uri_reserva, 'uri_buy':uri_buy})
