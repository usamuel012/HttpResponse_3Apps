from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Jason(request):
    return HttpResponse('<h1>Welcome</h1>')
def Eric(request):
    return HttpResponse('<marquee>Rave</marquee>')
