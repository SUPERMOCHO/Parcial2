from django import forms
from django.forms import ModelForm
from .models import nomagente 

class registro_nomAgenteForm(ModelForm):
	class Meta:
		model=nomagente
		fields=['id', 'nombre', 'apellido', 'telefono', 'placa']