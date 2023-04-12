from django import template

register = template.Library()

@register.inclusion_tag('template_tags/dropdown.html', takes_context=True)
def draw_dropdown(context, item):  # inclusion tag for drawing dropdown in menu
    full_path = context.request.get_full_path()
    return {'item': item, 'full_path': full_path}