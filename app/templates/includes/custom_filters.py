from django import template

register = template.Library()

@register.filter
def kg_to_oz(value):
    ounces = value * 35.273962
    return round(ounces, 3)
