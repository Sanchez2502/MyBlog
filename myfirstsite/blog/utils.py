from django.db.models import Count

from .models import *

menu = [{'title': "Головна", 'url_name': 'home'},
        {'title': "Додати нову статтю", 'url_name': 'add_article'},
        # {'title': "Зворотній зв'язок", 'url_name': 'contact'},

        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('puzzle'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['categories'] = categories
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context
