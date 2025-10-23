from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre', 'apellido', 'fecha_nacimiento', 'fecha_contratacion',
            'telefono', 'email', 'direccion', 'salario', 'rol', 'foto'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }