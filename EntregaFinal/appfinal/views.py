from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from appfinal.models import *

def inicio(request):
    return render(request,"appfinal/index.html")
def candidatos(request):
    return HttpResponse("Estas en candidatos")
def recomendadores(request):
    return HttpResponse("Estas en recomendadores")
def reclutadores(request):
    return HttpResponse("Estas en reclutadores")
def clientes(request):
    return HttpResponse("Estas en clientes")
# Create your views here.
