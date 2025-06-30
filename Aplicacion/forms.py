

from django import forms
from .models import Customers
from django.forms.widgets import HiddenInput

CRITERIO_CUMPLEANHOS = (
    ("", ""), ("hoy", "Hoy"), ("esta_semana", "Esta semana"), 
    ("este_mes", "Este mes")
    )

CRITERIO_ORDENAR = (("",""), ("nombre", "Por nombre"), ("company", "Por compañía"), 
                    ("cumpleanhos_actual", "Por cumpleaños"), ("fecha_interaccion", "Por interacción"))

class BuscaCustomersForm(forms.ModelForm):
    criterio_cumpleanhos = forms.ChoiceField(choices=CRITERIO_CUMPLEANHOS, label="Cumpleaños")
    criterio_ordenar = forms.ChoiceField(choices=CRITERIO_ORDENAR, label="Ordenar")

    class Meta:
        model = Customers
        fields = ("nombre", "criterio_cumpleanhos", "criterio_ordenar", )

    def __init__(self, *args, **kwargs):
        super(BuscaCustomersForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['criterio_cumpleanhos'].required = False
        self.fields['criterio_ordenar'].required = False
