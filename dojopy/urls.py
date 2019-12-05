from django.contrib import admin
from django.urls import path, include, path
from startup import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto', csrf_exempt(views.contact), name='contact'),
    path('', include('startup.urls')),
    path('startup/', include('startup.urls')),
    path('mentor', include('mentor.urls')),
    path('@', include('mentor.urls')),
    path('blog', include('blog.urls')),
    path('shop', include('shop.urls')),
]
