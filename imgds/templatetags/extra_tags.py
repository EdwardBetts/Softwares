from django import template
register = template.Library()

@register.filter
def hash(h, key):
    return h.get(key)

@register.filter
def image(h, key):
    if key in h:
        return h[key].image
