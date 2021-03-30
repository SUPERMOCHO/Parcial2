from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import administrador
from .forms import registroForm
from .forms1 import registro_nomAgenteForm
from .models import nomagente
# Create your views here.

def registro(request):
	data={
		'form':registroForm()
	}
	if request.method=='POST':
	 formulario=registroForm(request.POST) 
	 if formulario.is_valid():
	 	formulario.save()
	 	data['mensaje']="Registro guardado correctamente"
	return render(request, "registro.html", data)
	

def Modificar_registro(request,id):
	registro=administrador.objects.get(id=id)
	data={
			'form':registroForm(instance=registro)
		}
	if request.method=='POST':
			formulario=registroForm(data=request.POST, instance=registro)
			if formulario.is_valid():
				formulario.save()
				data['mensaje']="Modificado correctamente"
				data['form']=formulario


	return render(request, "cargar.html", data)


def Eliminar_registro(request, id):
	registro=administrador.objects.get(id=id)
	registro.delete()
	
	return HttpResponse("Registro eliminado")



def registronom_agente(request):
	data={
		'form':registro_nomAgenteForm()
	}
	if request.method=='POST':
	 formulario=registro_nomAgenteForm(request.POST) 
	 if formulario.is_valid():
	 	formulario.save()
	 	data['mensaje']="Registro del Agente de Transito guardado correctamente"
	return render(request, "registro.html", data)


def Modificar_Agente(request,id):
	registronom_agente=nomagente.objects.get(id=id)
	data={
			'form':registro_nomAgenteForm(instance=registronom_agente)
		}
	if request.method=='POST':
			formulario=registro_nomAgenteForm(data=request.POST, instance=registronom_agente)
			if formulario.is_valid():
				formulario.save()
				data['mensaje']="Modificado los datos del Agente de Transito correctamente"
				data['form']=formulario


	return render(request, "cargar.html", data)



def Eliminar_registroAgente(request, id):
	registronom_agente=nomagente.objects.get(id=id)
	registronom_agente.delete()
	
	return HttpResponse("Registro eliminado")






	