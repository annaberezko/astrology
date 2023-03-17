from django import template
from astro_app.models import Pages
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu_items = Pages.objects.all()
    href = context['request'].get_full_path()
    active_href = 0
    for i in menu_items:
        if i.title in href:
            active_href = i.id

    return {
        'menu': menu_items,
        'active_href': active_href
    }


@register.simple_tag()
def info(value):
    return Pages.objects.get(id=value)
