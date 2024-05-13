from django.contrib import admin

# Register your models here.
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author__username']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'created_at']
    search_fields = ['user__username', 'article__title']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'