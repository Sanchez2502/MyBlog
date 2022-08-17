from django import template
from blog.models import *

register = template.Library()


@register.simple_tag(name='getcategories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.simple_tag()
def is_like(article, user):
    try:
        liked = Likes.objects.get(puzzle=article, user=user)
    except:
        liked = False
    return liked


@register.simple_tag()
def is_favorite(article, user):
    try:
        favorited = Favorites.objects.get(puzzle=article, user=user)
    except:
        favorited = False
    return favorited
