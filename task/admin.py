from django.contrib import admin


from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'data')


admin.site.register(Task, TaskAdmin)