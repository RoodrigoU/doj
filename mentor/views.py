from django.shortcuts import render

# Create your views here.
def mentor(request):
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        mobile = ''
    return render(request, 'base_mentor.html', {'mobile': mobile})
