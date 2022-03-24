
from django.contrib import admin

from demo.main.models import Todo, Category


# authentication is built in in django




@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
