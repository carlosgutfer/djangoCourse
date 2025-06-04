from django import template

register = template.Library()

@register.filter
def get_field(obj, field_name):
    return getattr(obj, field_name, '')

@register.simple_tag(takes_context=True)
def sort_link(context, field_name):
    current_sort = context.get('current_sort', '')
    direction = ''
    icon = ''
    if current_sort == field_name:
        direction = f"-{field_name}"
        icon = '↓'
    elif current_sort == f"-{field_name}":
        direction = field_name
        icon = '↑'
    else:
        direction = field_name
    return f'?sort={direction}|{icon}'

@register.filter(name='zip_lists')
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def split(value, delimiter):
    return value.split(delimiter)