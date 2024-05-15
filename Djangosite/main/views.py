from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseNotFound
from .forms import FeedbackForm
from .models import *



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
    }

    return render(request, 'main/index.html', context=context)

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'main/projects.html',{'title': 'My site', 'Projects': projects})

def contact(request):
    if request.method == 'POST':
        feedbackForm = FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            print(feedbackForm.cleaned_data)
    feedbackForm = FeedbackForm()     
    return render(request, 'main/contact.html',{'form': feedbackForm,'title': 'My site'})

def showProject(request, project_slug):
    project = get_object_or_404(Projects, slug = project_slug)

    context = {
        'title': project.projName, 
        'Project' : project,
    }

    return render(request, 'main/project.html', context=context)

