from django.shortcuts import render


def home(request):
    # obj = ModelSaludo.objects.all()
    # obj = obj.values()
    # return HttpResponse('<h1> ¿hola te gusta mi pagina? </h1>')
    return render(request, 'home/index.html', {})
