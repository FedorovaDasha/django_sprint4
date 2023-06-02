from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Location, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'preview',
        'is_published',
        'location',
        'category',
        'author',
    )
    list_editable = (
        'is_published',

    )
    search_fields = ('title',)
    list_filter = (
        'category',
        'location',
    )
    list_display_links = ('title',)
    readonly_fields = ['preview']

    def preview(self, object):
        if object.image:
            return mark_safe(
                f'<img src="{object.image.url}" style="max-height: 100px;">'
            )
        else:
            return 'Нет фото'
    preview.short_description = 'Миниатюра'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author'
    )
    search_fields = ('text__startswith', )


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Location)
admin.site.register(Comment, CommentAdmin)
