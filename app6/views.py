from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sam(request):
    return HttpResponse('This is  a new..')
def Stone(request):
    return HttpResponse('<marquee>Hello World</marquee>')


