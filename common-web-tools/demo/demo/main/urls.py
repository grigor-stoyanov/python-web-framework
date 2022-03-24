from django.urls import path

from demo.main.views import index, ProfilesListView

urlpatterns = [
    path('', index, name='index'),
    path('', ProfilesListView.as_view(), name='profiles')
]
import demo.main.signals
