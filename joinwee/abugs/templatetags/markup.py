import markdown as md

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='markdown')
def markdown(value, arg=''):
    if not value:
        return ''
    extensions = []
    if arg == 'safe':
        extensions = ['extra']
    return mark_safe(md.markdown(value, extensions=extensions))
