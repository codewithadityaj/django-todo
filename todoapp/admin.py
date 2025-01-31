from django.contrib import admin


'''# Register your models here.
from django.contrib import admin'''
from .models import todoapp

class todoappAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed']  # fields to show in the list view
    search_fields = ['title']  # enable search by title
    list_filter = ['completed']  # add a filter sidebar to filter by completed status

admin.site.register(todoapp, todoappAdmin)
