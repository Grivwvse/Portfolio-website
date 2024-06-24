from django import template
from main.models import Person
from main.models import Site_settings
from main.views import menu


register = template.Library()

@register.simple_tag()
def get_menu():
    return menu

@register.simple_tag()
def get_person():
    person = Person.objects.filter(active=True).first()
    return person

@register.simple_tag()
def get_site_settings():
    settings = Site_settings.objects.first()
    return settings