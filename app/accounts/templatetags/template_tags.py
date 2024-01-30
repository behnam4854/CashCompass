# template_tags.py

from django import template

register = template.Library()

@register.filter
def subtract(value1, value2):
   return int(value1) - int(value2)