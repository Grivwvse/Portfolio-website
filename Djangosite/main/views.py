from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from .models import Person
from .models import Skills
from .models import Education
from .models import Experience
from .models import Projects
import datetime

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Проекты", 'url_name': 'projects'},
        {'title': "Контакты", 'url_name': 'contact'}]

def index(request):
    person =  Person.objects.all()
    skills = Skills.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    
    context = {
        'title': 'My site', 
        'Person': person[0], 
        'Skills': skills, 
        'Education':education, 
        'Experience' :experience,
        'menu': menu
    }

    return render(request, 'main/index.html', context=context)

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'main/projects.html',{'title': 'My site', 'Projects': projects, 'menu': menu})

def contact(request):
    return HttpResponse("Contacts")

def showPost(request, project_id):
    return HttpResponse("showPost = {project_id}")

