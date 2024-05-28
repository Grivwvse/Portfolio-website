from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', MainProjects.as_view(), name='projects'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('project/<slug:project_slug>/', ShowProject.as_view(), name='project'),
]

