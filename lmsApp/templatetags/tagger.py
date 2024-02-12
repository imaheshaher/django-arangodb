from django import template
import json
register = template.Library()

@register.simple_tag
def underscoreTag(obj, attribute):
    if obj[attribute] is not None:
        return obj[attribute]
    # Handle other cases if needed
    return None  # Or raise an exception