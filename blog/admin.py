from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'count_views', 'created_at')
    search_fields = ('count_views', 'created_at',)
