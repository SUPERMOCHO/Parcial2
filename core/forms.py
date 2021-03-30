from django import forms
from django.forms import ModelForm
from .models import administrador 

class registroForm(ModelForm):
	class Meta:
		model=administrador
		fields=['id', 'nombre', 'apellido', 'telefono']