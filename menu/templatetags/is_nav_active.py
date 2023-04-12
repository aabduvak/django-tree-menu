from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_nav_active(context, path):  # simple tag for defining is item active
    if path in context.request.get_full_path():
        return 'active'
    else:
        return None