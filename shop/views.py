from django.shortcuts import render

# Create your views here.
def shop(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller%20Python."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller%20Python."

    return render(request, 'shop.html', {'uri_whatsapp': uri_whatsapp})
