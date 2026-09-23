from django import forms
from .models import Mascota, Propietario


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "edad", "propietario"]


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ["nombre", "telefono", "email"]