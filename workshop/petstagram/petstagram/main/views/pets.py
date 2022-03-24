from django.views.generic import CreateView, UpdateView, DeleteView

from petstagram.main.forms.pet_forms import CreatePetForm, DeletePetForm


class CreatePetView(CreateView):
    template_name = 'main/pet_create.html'
    form_class = CreatePetForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    # def form_valid(self, form):
    #     user = self.request.user
    #     return super().form_valid(form)


class EditPetView(UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = CreatePetForm


class DeletePetView(DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm
