from django import template
from blog.models import *

register = template.Library()

@register.simple_tag(name='getcategories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)



@register.inclusion_tag('blog/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {"categories": categories, "category_selected": category_selected}


@register.simple_tag()
def count_likes(pk):
    return Likes.objects.filter(pk=pk).count()

