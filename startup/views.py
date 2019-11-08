from django.shortcuts import render

# Create your views here.
def home(request):
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        mobile = ''
    return render(request, 'base.html', {'mobile': mobile})
