from django import template
import json
register = template.Library()

@register.simple_tag
def underscoreTag(obj, attribute):
    if type(obj) == dict:
        if obj.get(attribute) is not None:
            return obj.get(attribute)
        return ''
    if obj[attribute] is not None:
        return obj[attribute]
    
    # Handle other cases if needed
    return ''  # Or raise an exception



@register.simple_tag
def underscoreBookTag(obj, attribute):
    if obj and obj[attribute]:
        return obj[attribute]
    if obj.get(attribute) is not None:
        return obj[attribute]
    # Handle other cases if needed
    return {}  # Or raise an exception