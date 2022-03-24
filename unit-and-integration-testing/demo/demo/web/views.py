from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView

from demo.web.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile/create.html'

    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': self.object.pk})


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/list.html'
    context_user_key = 'user'
    no_logged_in_user_value = 'No User'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context[self.context_user_key] = self.request.user.username
        else:
            context[self.context_user_key] = self.no_logged_in_user_value
        return context

    def get_queryset(self):
        return super().get_queryset() \
            .prefetch_related('') \
            .filter()


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/details.html'
