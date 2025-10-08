from django.http import HttpResponse

def fake_admin_login(request):
    return HttpResponse("صفحه‌ی مدیریت وجود ندارد. لطفاً مسیر را بررسی کنید.")
