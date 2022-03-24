from django import forms
from django.forms import modelform_factory

from demo.web.models import Profile


# no point to test modelforms
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# we can even use django's modelform Factory
ProfileForm2 = modelform_factory(Profile, fields='__all__')

