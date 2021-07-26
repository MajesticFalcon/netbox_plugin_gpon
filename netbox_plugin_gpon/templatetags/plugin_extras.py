from django import template
import re

register = template.Library()


@register.filter()
def plugin_viewname(model, action):
    """
    Return the view name for the given model and action. Does not perform any validation.
    """
    return f"plugins:{model._meta.app_label}:{model._meta.model_name}_{action}"

@register.filter()
def plugin_remove_cidr(ip):
    return str(re.sub('/.*', '', str(ip)))
