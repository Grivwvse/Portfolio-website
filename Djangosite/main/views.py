from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from .models import Person
from .models import Skills
from .models import Education
from .models import Experience
import datetime

def index(request):
    person =  Person.objects.all()
    skills = Skills.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()

    return render(request, 'main/index.html',{'title': 'My site', 'Person': person[0], 'Skills': skills, 'Education':education, 'Experience' :experience})

def projects(request):
    return render(request, 'main/projects.html')