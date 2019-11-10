from django.shortcuts import render
from .models import ModelContact
from django.http import JsonResponse

# Create your views here.
def home(request):
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        mobile = ''
    return render(request, 'base.html', {'mobile': mobile})


def contact(request):
    name = request.POST.get('username', '')
    email = request.POST.get('email', '')
    ModelContact.objects.get_or_create(name=name, email=email)
    return JsonResponse({'status': 'ok'})
