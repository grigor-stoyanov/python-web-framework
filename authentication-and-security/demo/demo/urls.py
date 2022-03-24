from django.contrib import admin
from django.urls import path

from demo.main.views import index, IndexView, IndexTemplateView, MyListView, TodoDetails, TodoCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index func-based'),
    path('cbv/', IndexView.as_view(), name='index class-based'),
    path('cbv2/', IndexTemplateView.as_view(), name='index class-based 2'),
    path('cbv3/', MyListView.as_view(), name='index class-based 3'),
    path('cbv4/<int:pk>/', TodoDetails.as_view(), name='todo details'),
    path('cbv5/', TodoCreate.as_view(), name='create todo'),
]
