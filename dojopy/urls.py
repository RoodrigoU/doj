from django.contrib import admin
from django.urls import path, include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startup.urls')),
    path('mentor/', include('mentor.urls')),
    path('@', include('mentor.urls')),
    path('blog', include('blog.urls')),
    path('shop', include('shop.urls')),
]
