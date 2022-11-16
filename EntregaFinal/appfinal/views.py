from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from appfinal.models import *

def inicio(request):
    return render(request,"appfinal/index.html")
def candidatos(request):
    return render(request,"appfinal/candidatos.html")
def recomendadores(request):
    return render(request,"appfinal/recomendadores.html")
def reclutadores(request):
    return render(request,"appfinal/reclutadores.html")
def clientes(request):
    return render(request,"appfinal/clientes.html")
# Create your views here.
