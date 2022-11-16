from django.db import models
from datetime import datetime

# Create your models here.
class Candidatos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)
    edad=models.IntegerField()

class Recomendadores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    itrecruiter=models.BooleanField(default=False)


class Reclutadores(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    manager=models.CharField(max_length=40)

class Clientes(models.Model):
    nombreempresa=models.CharField(max_length=40)
    descempresa=models.CharField(max_length=120)
    ofertaactiva=models.BooleanField(default=False)

# Create your models here.
