from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseNotFound
from .forms import FeedbackForm
from .models import *

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def decrypt_password(encrypted_password):
    decrypted_password = ""
    for char in encrypted_password:
        decrypted_password += chr(ord(char) - 6)
    return decrypted_password

def sendMail(feedbackForm):
    mailNotification = MailNotification.objects.filter(isActive = True)

    text = feedbackForm.get('fullName') + "\n" + feedbackForm.get('mail') + "\n" + feedbackForm.get('message')
    part1 = MIMEText(text, "plain")

    message = MIMEMultipart("alternative")

    for m in mailNotification:
        message["Subject"] = "Обратная связь"
        message["From"] = m.mailLogin
        message["To"] = m.mailLogin
        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.mail.ru", 465, context=context) as server:
            server.login(m.mailLogin, decrypt_password(m.mailPassword))
            server.sendmail( m.mailLogin, m.mailLogin, message.as_string())

    
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
        'Skills': skills, 
        'Education':education, 
        'Experience' :experience,
    }

    return render(request, 'main/index.html', context=context)

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'main/projects.html',{'title': 'My site', 'Projects': projects})

def contact(request):
    contacts = Contacts.objects.all()
    if request.method == 'POST':
        feedbackForm = FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            if '@' in feedbackForm.cleaned_data['mail']:
                try:
                    sendMail(feedbackForm.cleaned_data)
                    feedbackForm.add_error(None, 'Успешная отправка сообщения!')
                except:
                    feedbackForm.add_error(None, 'Ошибка отправки сообщения')
            else:
                feedbackForm.add_error(None, 'Некорректно указан почтовый ящик')
    else:
        feedbackForm = FeedbackForm()     
    return render(request, 'main/contact.html',{'form': feedbackForm,'title': 'My site', 'contacts': contacts[0]})

def showProject(request, project_slug):
    project = get_object_or_404(Projects, slug = project_slug)

    context = {
        'title': project.projName, 
        'Project' : project,
    }

    return render(request, 'main/project.html', context=context)

