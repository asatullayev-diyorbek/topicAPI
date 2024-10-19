from django.contrib import admin

from .models import Topic, Comment


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'topic', 'content', 'reply', 'created_at', 'updated_at']
    list_display_links = ['id', 'user']
