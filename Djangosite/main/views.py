from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

def index(request):
    return render(request, 'main/index.html',{'title': 'My site'})

def projects(request):
    return render(request, 'main/projects.html')