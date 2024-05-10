from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='home'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
    path('project/<int:project_id>/', showPost, name='project'),
]

