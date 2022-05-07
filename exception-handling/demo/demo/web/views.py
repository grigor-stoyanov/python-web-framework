from django import views
from django.http import HttpResponse
from django.db.models import Model
from django.shortcuts import render

from demo.web.models import Todo, Category


class AppException(Exception):
    pass
def no_exception_view(response):
    return HttpResponse('No Error View')
def exception_view(response):
    # raises db.model.DoesNotExist()
    try:
        t = Todo.objects.get(pk=4)
    except Model.DoesNotExist:
        # Handle DoesNotExist => show 404
        pass

    # v2 without exceptions(not preferred)
    todo = Todo.objects.filter(pk=4)
    if not todo:
        pass

    # get must return exactly 1 object
    # raises MultipleObjectsReturned
    t = Todo.objects.get(title__contains='todo')


def raises_exception(request):
    # in debug exceptions raise as serverError500
    raise TypeError('Object has invalid id: valid id are 1 3 5 7')


# exception applications:
# handle different funcionalities
def get_or_create_category(name):
    try:
        return Category.objects.get(name=name)
    except Model.DoesNotExist:
        return Category.objects.create(name=name)


def create_todo(request):
    category_name = request.POST.get('category')
    # category = Category.objects.get(name=category_name)
    category = get_or_create_category(category_name)


# reraise exception for additional context
# catch exceptions in a middleware and hide them from user
def internal_error(request):
    return HttpResponse('An error occured,please try again!')


class InternalErrorView(views.View):
    def get(self, request):
        return HttpResponse('Án error occured,please try again!')

# issue our application fails silently anti-pattern
# that is where logging comes in allowing us to reproduce bugs
# logging can be done on console(for development),saved on file,or server logging

