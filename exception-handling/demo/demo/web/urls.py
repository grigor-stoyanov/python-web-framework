from django.urls import path

from demo.web.views import exception_view, raises_exception, no_exception_view


class MyView:
    pass


urlpatterns = [
    path('', exception_view, name='exception view'),
    # ViewDoesNotExistException
    path('asd/', MyView),
    path('exception/', raises_exception),
    path('no-error/', no_exception_view)
]
