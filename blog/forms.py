from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .models import *


class CreateNewArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категорія не вибрана"

    class Meta:
        model = Puzzle
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 20}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('Довжина перевищує 50 символів')
        return name


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class SharePuzzleForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.user2.add_error({'user_is_not_valid': "Ви не можете радити собі статті"})
#         # print(self.errors())
#
#     def form_invalid(self, form):
#         return super(SharePuzzleForm, self).form_invalid(form)

    # def form_valid(self, form):
    #
    #
    #
    #     less_than_one = form.cleaned_data.get('less_than_one')
    #     if less_than_one > 1:
    #         form.add_error('less_than_one', forms.ValidationError('Can not be greater than one'))
    #         return super(SharePuzzleForm, self).x
    #     return super(SharePuzzleForm, self).form_valid(form)

    # def is_valid(self):
    #     user1 = self.cleaned_data['user1']
    #     user2 = self.cleaned_data['user2']
    #
    #     if user2 == user1:
    #         raise ValidationError('Ви не можете радити собі статті')
    #     else:
    #         super().is_valid()

    # class Meta:
    #     model = Shares
    #     fields = ('user2', 'puzzle')
        # form.add_error('user2', forms.ValidationError("Ви не можете радити собі статті"))
        # error_messages={
        #     NON_FIELD_ERRORS:{
        #         'user_is-not-valid': "Ви не можете радити собі статті"
        #     }
        # }

    # def clean_user2(self):
    #     user1 = self.cleaned_data['user1']
    #     user2 = self.cleaned_data['user2']
    #     # forms1 = form.save(commit=False)
    #     # user1 = forms1.user1
    #     if user2 == user1:
    #         raise form.non_field_errorsValidationError('Ви не можете радити собі статті')
    #     return user1
    #

    # def clean_user2(self):
    #     print(self)
    #     user1 = self.cleaned_data['user1']
    #     user2 = self.cleaned_data['user2']
    #     # forms1 = form.save(commit=False)
    #     # user1 = forms1.user1
    #     if user2 == user1:
    #         raise ValidationError('Ви не можете радити собі статті')
    #     return user2
