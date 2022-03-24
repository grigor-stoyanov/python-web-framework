from django import forms

from petstagram.common.helpers import BootStrapFormMixin
from petstagram.main.models import PetPhoto


class CreatePhotoForm(BootStrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')

        widgets = {
            'photo': forms.FileInput(
                attrs={'class': 'form-control-file'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter Description'}
            )
        }


class EditPhotoForm(BootStrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Enter Description'}
            )
        }


class DeletePhotoForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = PetPhoto
        fields = ()
