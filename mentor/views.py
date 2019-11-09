from django.shortcuts import render

# Create your views here.
def mentor(request):
    try:
        mobile = request.user_agent.is_mobile
    except:
        mobile = ''
    return render(request, 'base_mentor.html', {'mobile': mobile})


def taller_python(request):
    try:
        mobile = request.user_agent.is_mobile
    except:
        mobile = ''
    return render(request, 'taller_python.html', {'mobile': mobile})
