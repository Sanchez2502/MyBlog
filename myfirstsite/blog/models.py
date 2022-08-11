from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Puzzle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Опис")
    photo = models.ImageField(upload_to="photos", verbose_name="Фото")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час останньої зміни")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорія")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    class Meta:
        verbose_name = 'Головоломка'
        verbose_name_plural = 'Головоломки'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']


# class Comments(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
#     text = models.TextField(blank=True, verbose_name="Текст коментаря")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час останньої зміни")
#     puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, verbose_name="Стаття")
#
#     def __str__(self):
#         return f"{self.user}"
#
#     class Meta:
#         verbose_name = 'Коментар'
#         verbose_name_plural = 'Коментарі'
#         ordering = ['id']


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, verbose_name="Стаття")

    def __str__(self):
        return f'{self.user} : {self.puzzle}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ['puzzle']
