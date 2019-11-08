from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('startup', include('startup.urls')),
    path('mentor', include('mentor.urls')),
    path('blog', include('blog.urls'))
]
