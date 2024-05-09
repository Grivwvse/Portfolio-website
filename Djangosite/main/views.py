from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from .models import Person

def index(request):
    person =  Person.objects.all()
    return render(request, 'main/index.html',{'title': 'My site', 'Person': person[0]})

def projects(request):
    return render(request, 'main/projects.html')