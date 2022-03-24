from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from petstagram.auth_app.models import Profile
from petstagram.common.helpers import BootStrapFormMixin
from petstagram.main.models import PetPhoto


class EditProfileForm(BootStrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.GENDER_DO_NOT_SHOW
        self.fields['birth_date'].input_type = 'date'

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                    'placeholder': 'Enter Date of Birth',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),
            'gender': forms.Select(
                choices=Profile.GENDERS,
            )
        }


class CreateProfileForm(BootStrapFormMixin, UserCreationForm):
    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LENGTH)
    last_name = forms.CharField(max_length=Profile.LAST_NAME_MAX_LENGTH)
    picture = forms.URLField()
    birth_date = forms.DateField()
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDERS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.GENDER_DO_NOT_SHOW

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            birth_date=self.cleaned_data['birth_date'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user, )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'description', 'picture')
        # the hard way to style form
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name',
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Email'
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    # we will overwrite save method
    def save(self, commit=True):
        # self.instance = profile
        pets = self.instance.pet_set.all()
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ('first_name', 'last_name', 'email', 'profile_picture', 'description', 'birth_date', 'gender')
