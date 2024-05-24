from django import template
from main.models import Person
from main.views import menu

register = template.Library()

@register.simple_tag()
def get_menu():
    return menu

@register.simple_tag()
def get_person():
    person = Person.objects.all()
    return person[0]