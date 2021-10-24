from django import template

register = template.Library()

@register.simple_tag
def get_data(model, prop):
   return getattr(model, str(prop))