from django.contrib import admin
from .models import Task

class TaskInline(admin.StackedInline):
    model = Task
    extra = 5

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_nm']}),
        (None, {'fields': ['task_text']}),
        (None, {'fields': ['comp_flg']}),
    ]

admin.site.register(Task)
