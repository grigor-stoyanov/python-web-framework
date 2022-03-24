from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from petstagram.auth_app.forms.profile_forms import CreateProfileForm, EditProfileForm
from petstagram.auth_app.models import Profile

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto, Pet


class ProfileDetailsView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a profile
        profile_pets = Pet.objects.filter(user=self.object.user_id)
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=profile_pets).distinct()
        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_images_count = len(pet_photos)
        context.update({
            'my_pets': profile_pets,
            'total_likes_count': total_likes_count,
            'total_images_count': total_images_count,
            'is_owner': self.object.user_id == self.request.user.id
        })
        return context


class UserRegisterView(RedirectToDashboard, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('auth:profile', kwargs={'pk': self.object.pk})


class ChangeUserPasswordView(PasswordChangeView):
    # template_name = 'accounts/change_password.html'
    pass