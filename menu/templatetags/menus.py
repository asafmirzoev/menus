from django import template
from django.utils.safestring import mark_safe

from menu.models import Menu
from menu.utils import generate_menu


register = template.Library()


@register.simple_tag(takes_context=True)
def render_menu(context: dict, menu_slug: str):
    menu: Menu = Menu.objects.get(slug=menu_slug)
    html: str = generate_menu(menu.pk, menu.category_set.filter(parent__isnull=True), context['request'].path)
    return mark_safe(html)