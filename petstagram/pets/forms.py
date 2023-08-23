from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'personal_pet_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

        labels = {
            'name': 'Pet Name:',
            'personal_pet_photo': 'Link to Image:',
            'date_of_birth': 'Date of birth:'
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'readonly'
            field.widget.attrs['readonly'] = 'readonly'
