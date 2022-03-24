from django.contrib.auth import login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.shortcuts import render

# django gives us login and logout views by default with forms
# there is no need to log our users like this
from django.urls import reverse_lazy
from django.views import generic as views

from demo.auth_app.models import Profile


# django adds next=/auth/restricted/ next redirect to successful login
class RestrictedView(LoginRequiredMixin, views.TemplateView):
    template_name = 'index.html'


def my_view(request):
    user = None
    login(request, user)


# good enough to create registry
# class UserRegistrationView(views.CreateView):
#     model = User


# returns our own model instead of base one
UserModel = get_user_model()


# one way to combine profile and user models in our form is extending the registration form
class UserRegisterForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(max_length=25)

    class Meta:
        # need to give the user model
        model = UserModel
        # fields = ('username', 'first_name')
        # for our customised authentication model userRegistrationForm has hardcoded model = User
        # we need to extend it with model = UserModel!
        fields = ('email',)

    # def clean_first_name(self):
    #     return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)
        # now we add profile with user to database!
        profile = Profile(
            **self.cleaned_data,
            user=user
        )
        # profile = Profile(
        #     first_name=self.cleaned_data['first_name'],
        #     user=user,
        # )
        if commit:
            profile.save()
        return user

    # or we make a new one (more complicated)
    # class ProfileCreateForm(forms.ModelForm):
    #     class Meta:
    #         model = Profile
    #         fields = ('first_name',)


class UserRegistrationView(views.CreateView):
    # model with all the necessary fields
    # extensible by inheriting UserCreationForm
    # form_class = auth_forms.UserCreationForm
    form_class = UserRegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    # we show our additional profile form
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_form'] = ProfileCreateForm()
    #     return context

    # add login functionality to register
    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    # template_name = 'auth/login.html'
    template_name = 'registration/login.html'

    # next_page = reverse_lazy('index')
    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogout(LogoutView):
    next_page = reverse_lazy('index')
