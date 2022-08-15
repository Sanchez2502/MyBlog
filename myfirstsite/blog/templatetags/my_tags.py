from django import template
from blog.models import *

register = template.Library()


@register.simple_tag(name='getcategories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


# @register.simple_tag(takes_context=True)
# def is_like(context, article, user):
#     print(article)
#     print(user)
#
#     try:
#         liked = Likes.objects.get(puzzle=article, user=user)
#     except:
#         liked = False
#     return liked
