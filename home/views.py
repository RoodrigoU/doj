from django.shortcuts import render
from django.http import JsonResponse
from .models import ModelContact


def home(request):
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        mobile = ''
    # obj = ModelSaludo.objects.all()
    # obj = obj.values()
    # return HttpResponse('<h1> ¿hola te gusta mi pagina? </h1>')
    return render(request, 'home/index.html', {'mobile': mobile})


def contact(request):
    name = request.POST.get('username', '')
    email = request.POST.get('email', '')
    ModelContact.objects.get_or_create(name=name, email=email)
    return JsonResponse({'status':'ok'})
