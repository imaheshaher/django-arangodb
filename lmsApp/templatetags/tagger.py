from django import template
import json
register = template.Library()

@register.simple_tag
def underscoreTag(obj, attribute):
    if hasattr(obj, attribute):
        return getattr(obj, attribute)
    # Handle other cases if needed
    return None  # Or raise an exception