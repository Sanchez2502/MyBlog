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


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, verbose_name="Стаття")

    def __str__(self):
        return f'{self.user} : {self.puzzle}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ['puzzle']

    def save(self, *args, **kwargs):
        if Likes.objects.filter(user=self.user, puzzle=self.puzzle):
            return
        else:
            super().save(*args, **kwargs)


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, verbose_name="Стаття")

    def str(self):
        return f'{self.user} : {self.puzzle}'

    def save(self, *args, **kwargs):
        if Favorites.objects.filter(user=self.user, puzzle=self.puzzle):
            return
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Улюблене'
        verbose_name_plural = 'Улюблені'
        ordering = ['user']


class Shares(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Відправник", related_name="Poster")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Отримувач", related_name="Geter")
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, verbose_name="Стаття")

    def str(self):
        return f'{self.user2} : {self.puzzle}'

    class Meta:
        verbose_name = 'Поширені'
        verbose_name_plural = 'Поширені'
        ordering = ['user2']

    def save(self, *args, **kwargs):
        if Shares.objects.filter(user1=self.user1, user2=self.user2, puzzle=self.puzzle):
            return
        else:
            super().save(*args, **kwargs)

