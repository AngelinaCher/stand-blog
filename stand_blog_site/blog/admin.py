from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Tag, Post, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Регистрация модели Поста """
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    list_display = ['id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views']
    list_display_links = ['id', 'title']
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at', 'author')
    list_per_page = 7

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_descriptions = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Регистрация модели Категории """
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    list_per_page = 7


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Регистрация модели Тега """
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    list_per_page = 7


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Регистрация модели Обратной связи """
    pass
