from django.urls import path
from django.views.generic import TemplateView

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView
from petstagram.main.views.photos import like_pet, CreatePetPhotoView, PetPhotoDetails, EditPetPhotoView, \
    DeletePetPhotoView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('401/', TemplateView.as_view(template_name='main/401.html'), name='401'),


    path('pet/add/', CreatePetView.as_view(), name='create pet'),
    path('pets/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pets/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/details/<int:pk>/', PetPhotoDetails.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>', like_pet, name='like photo'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='create pet photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit pet photo'),
    path('photo/delete/<int:pk>/', DeletePetPhotoView.as_view(), name='delete pet photo')
]
