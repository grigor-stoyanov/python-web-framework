from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from petstagram.main.forms.photo_forms import CreatePhotoForm, DeletePhotoForm, EditPhotoForm
from petstagram.main.models import PetPhoto


def like_pet(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('pet photo details', pk)


class PetPhotoDetails(DetailView, LoginRequiredMixin):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class CreatePetPhotoView(CreateView, LoginRequiredMixin):
    model = PetPhoto
    template_name = 'main/photo_create.html'
    form_class = CreatePhotoForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(UpdateView):
    model = PetPhoto
    template_name = 'main/photo_edit.html'
    form_class = EditPhotoForm


class DeletePetPhotoView(DeleteView):
    model = PetPhoto
    template_name = 'main/photo_delete.html'
