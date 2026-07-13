import bleach
import markdown as md

from django import template
from django.utils.safestring import mark_safe

ALLOWED_TAGS = [
    'a', 'abbr', 'acronym', 'b', 'blockquote', 'br', 'code', 'dd', 'del',
    'dl', 'dt', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i',
    'img', 'li', 'ol', 'p', 'pre', 'strong', 'sub', 'sup', 'ul',
]

ALLOWED_ATTRS = {
    'a': ['href', 'title', 'rel'],
    'img': ['src', 'alt', 'title', 'width', 'height'],
}

register = template.Library()


@register.filter(name='markdown')
def markdown(value, arg=''):
    if not value:
        return ''
    extensions = ['extra']
    html = md.markdown(value, extensions=extensions)
    clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)
    return mark_safe(clean)
