from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('nargesi-1404-path/', admin.site.urls),
    path('', include('Main.urls')),      
    path('api/', include('Main.api.urls')),
]