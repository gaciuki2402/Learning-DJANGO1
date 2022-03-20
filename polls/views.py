from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context={}
    return render(request, "polls/index.html",context)

def about(request):
    context={}
    return render(request, "polls/about.html",context)


# Create your views here.
