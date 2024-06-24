from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', MainProjects.as_view(), name='projects'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('project/<slug:project_slug>/', ShowProject.as_view(), name='project'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
] + urlpatterns