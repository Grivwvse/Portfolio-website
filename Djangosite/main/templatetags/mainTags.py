from django import template
from main.models import *
from main.views import menu

register = template.Library()

@register.simple_tag()
def get_menu():
    return menu