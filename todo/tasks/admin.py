from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'complete')
    list_filter = ('created',)
    ordering = ('title', 'created')
    search_fields = ('title',)
