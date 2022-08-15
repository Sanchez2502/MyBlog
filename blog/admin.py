from django.contrib import admin

from .models import *


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_update')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'puzzle',)
    autocomplete_fields = ('user', 'puzzle',)
    list_display_links = ('puzzle',)
    search_fields = ('puzzle',)
    list_filter = ('user', 'puzzle',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'puzzle',)
    autocomplete_fields = ('user', 'puzzle',)
    list_display_links = ('puzzle',)
    search_fields = ('user',)
    list_filter = ('user', 'puzzle',)


# class ShareAdmin(admin.ModelAdmin):
#     list_display = ('user1', 'user2', 'puzzle',)
#     autocomplete_fields = ('user1',)
#     list_display_links = ('user1', 'user2', 'puzzle',)


admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Likes, LikeAdmin)
admin.site.register(Favorites, FavoriteAdmin)
# admin.site.register(Shares, ShareAdmin)
