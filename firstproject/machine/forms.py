from .models import Agregat
from django.forms import ModelForm, TextInput, DateTimeInput


# Привязываем форму к бд
class AgregatForm(ModelForm):

    class Meta:
        model = Agregat
        fields = ['agregat', 'date', 'update', 'vertolet']

        widgets = {
            "agregat": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата изготовления'
            }),
            "update": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата ремонта'
            }),
        }

    def __init__(self, vert_id):
        super(AgregatForm, self).__init__(self, vert_id)
        self.fields['vertolet'] = models.Vertolet.object.get(pk=vert_id)