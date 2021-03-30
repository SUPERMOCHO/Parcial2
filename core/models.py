from django.db import models

# Create your models here.

class administrador(models.Model):
    id=models.CharField(primary_key=True, max_length=20)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    telefono=models.CharField(max_length=40)


class nomagente(models.Model):
    id=models.CharField(primary_key=True,max_length=20)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    telefono=models.CharField(max_length=40)
    placa=models.CharField(max_length=10)

class comparendera(models.Model):
    consecutivo=models.CharField(max_length=20)
    


class turnos(models.Model):
    mañana=models.CharField(max_length=20)
    tarde=models.CharField(max_length=40)
    noche=models.CharField(max_length=40)