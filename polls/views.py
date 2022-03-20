from django.shortcuts import render
from django.http import HttpResponse

def lib(request):
    return HttpResponse("Hello,Welcome to the Libray.It's open 24/7")
    

# Create your views here.
