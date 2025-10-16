from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),  # مسیر جعلی ادمین
    path('secure-admin/', admin.site.urls),  # مسیر واقعی پنل ادمین
    path('', include('Main.urls')),          # مسیر اپ blog
    #path('account/', include('account.urls'))  # مسیر اپ account
    path('api/', include('Main.api.urls')),  # ارجاع به urls اپ api
]