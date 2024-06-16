from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("<html><head></head><body><h1>Hello World</h1></body></html>")