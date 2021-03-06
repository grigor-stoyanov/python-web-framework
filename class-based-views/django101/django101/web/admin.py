from django.contrib import admin

from django101.web.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
