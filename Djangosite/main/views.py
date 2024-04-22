from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from .models import Person

def index(request):
    person =  Person.objects.all()
    return render(request, 'main/index.html',{'title': 'My site', 'fullname': person[0].fullName})

def projects(request):
    return render(request, 'main/projects.html')