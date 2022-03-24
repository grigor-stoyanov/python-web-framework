from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.helpers import BootStrapFormMixin
from petstagram.main.models import Pet, PetPhoto


class CreatePetForm(BootStrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date is not None:
            if birth_date < self.MIN_DATE_OF_BIRTH or birth_date > self.MAX_DATE_OF_BIRTH:
                raise ValidationError('Date of birth out of range')

    class Meta:
        model = Pet
        fields = ('name', 'type', 'birth_date')
        widgets = {
            'name': forms.TextInput(
                attrs={"placeholder": "Enter Pet name"
                       }),
        }


class DeletePetForm(BootStrapFormMixin, forms.ModelForm):
    def save(self, commit=True):
        # self.instance = profile
        PetPhoto.objects.filter(tagged_pets=self.instance.pk).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ()
