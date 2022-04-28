from django.urls import path

from demo.web.views import IndexView

urlpatterns=[
    path('',IndexView.as_view(),name='index')
]