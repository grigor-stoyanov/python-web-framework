import datetime

from django import template

register = template.Library()


@register.filter()
def years_to_now(birth_date):
    return datetime.datetime.now().year - birth_date.year
