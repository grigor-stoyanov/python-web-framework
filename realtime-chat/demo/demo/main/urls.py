from django.urls import path

from demo.main.views import index, room

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
