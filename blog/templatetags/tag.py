from typing import Any

from django import template

register = template.Library()


@register.filter()
def mymedia(data: Any) -> str:
    """ image output """
    if data:
        return f'/media/{data}'
    return '#'
