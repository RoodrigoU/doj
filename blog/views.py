from django.shortcuts import render
from .models import ModelBlog
# from django.http import HttpResponse

def blog(request):
    obj = ModelBlog.objects.all()
    obj = obj.values()
    return render(request, 'blog/blog.html', {'data': obj})

def contact(request):
    return render(request, 'contacto.html')
