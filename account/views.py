from django.shortcuts import render
from ratelimit.decorators import ratelimit
from django.http import HttpResponse

@ratelimit(key='ip', rate='5/m', block=True)
def fake_admin_login(request):
    return HttpResponse("Something went wrong. Please try again later.")
