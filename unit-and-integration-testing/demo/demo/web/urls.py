from django.urls import path

from demo.web.views import ProfileCreateView, ProfileDetailsView, ProfileListView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('list/', ProfileListView.as_view(), name='profile list'),
]
