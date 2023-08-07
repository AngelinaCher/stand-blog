from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Tag, Post


# для формирования slug
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True
    list_display = ['id', 'title', 'slug', 'category', 'created_at',
                    'get_photo', 'views']
    list_display_links = ['id', 'title']
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views',
              'created_at', 'author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_descriptions = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
