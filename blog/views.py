from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.forms import ModelForm
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .utils import *


class Home(DataMixin, ListView):
    model = Puzzle
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Puzzle.objects.filter(is_published=True)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreateNewArticleForm
    template_name = 'blog/addarticle.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Додати нову статтю")
        return dict(list(context.items()) + list(c_def.items()))


class ShowArticle(DataMixin, DetailView):
    model = Puzzle
    template_name = 'blog/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        count_of_likes = {'count_of_likes': Likes.objects.filter(puzzle=context['article'].pk).count()}
        context.update(count_of_likes)

        c_def = self.get_user_context(title=context['article'])
        return dict(list(context.items()) + list(c_def.items()))


class PuzzleCategory(DataMixin, ListView):
    model = Puzzle
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Puzzle.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - ' + str(context['articles'][0].category),
                                      category_selected=context['articles'][0].category_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class AddLike(LoginRequiredMixin, View):
    model = Likes
    template_name = 'blog/article.html'
    context_object_name = 'articles'

    def post(self, request, pk, *args, **kwargs):
        puzzles = Likes.objects.filter(puzzle=pk)
        puzzle = get_object_or_404(Puzzle, pk=pk)

        for user in puzzles:
            if user.user == request.user:
                get_object_or_404(Likes, user=request.user, puzzle=pk).delete()
                break
        else:
            Likes.objects.create(user=request.user, puzzle=puzzle)
        return redirect(reverse('article', args=[puzzle.slug]))


class AddFavorite(LoginRequiredMixin, View):
    model = Favorites
    template_name = 'blog/article.html'
    context_object_name = 'articles'

    def post(self, request, pk, *args, **kwargs):
        puzzles = Favorites.objects.filter(puzzle=pk)
        puzzle = get_object_or_404(Puzzle, pk=pk)

        for user in puzzles:
            if user.user == request.user:
                get_object_or_404(Favorites, user=request.user, puzzle=pk).delete()
                break
        else:
            Favorites.objects.create(user=request.user, puzzle=puzzle)
        return redirect(reverse('article', args=[puzzle.slug]))


class ShowFavorite(DataMixin, ListView):
    paginate_by = 3
    model = Favorites
    template_name = 'blog/likes.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - Улюблені', )
        return dict(list(context.items()) + list(c_def.items()))


# class AddShare(LoginRequiredMixin, DataMixin, CreateView, ModelForm):
#     model = Shares
#     form_class = SharePuzzleForm
#     template_name = 'blog/addshare.html'
#     context_object_name = 'shares'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('home')
#     raise_exception = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Поділитись статтею")
#         return dict(list(context.items()) + list(c_def.items()))

    # def form_invalid(self, form):
    #     return super(form, self).form_invalid(form)
    #
    # def form_valid(self, form):
    #     # print(type(form))
    #     # user1 = {'user1': self.request.user}
    #     new_share = form.save(commit=False)
    #     new_share.user1 = self.request.user
    #     if new_share.user2 == new_share.user1:
    #         form.add_error('user2', forms.ValidationError("Ви не можете радити собі статті"))
    #         return self.form_invalid(form)
    #     new_share.save()
    #     # form.save()
    #     return redirect('add_share')




# class ShowShare(DataMixin, ListView):
#     paginate_by = 3
#     model = Shares
#     template_name = 'blog/shares.html'
#     context_object_name = 'articles'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Shares.objects.filter(user2=self.request.user)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Категорія - Улюблені', )
#         return dict(list(context.items()) + list(c_def.items()))


# {% if request.user.is_authenticated %}
# 		<form method="post">
# 			{% csrf_token %}
# 			<div>
# 				<button style="background: transparent; border: none; box-shadow: none;" type="submit">
# 					<input type="hidden" name="request" value="{{ request }}">
# 					<li><a href="{% url 'share_show'%}">Мені порадили</a></li>
# 				</button>
# 			</div>
# 		</form>
# 		{% endif %}       

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')

# def user_is_not_valid(form, request):
#     if form.save
