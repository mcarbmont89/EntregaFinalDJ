from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from appfinal.models import *
from appfinal.forms import CandidatoForm
from appfinal.forms import RecomendadorForm

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
def alta_candidatos(request):
    if request.method=="POST":
        formulario=CandidatoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            candidato=Candidatos(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"],edad=data["edad"])
            candidato.save()
            return render(request,"appfinal/index.html")
        pass 
    else:
        formulario = RecomendadorForm()
    contexto = {"formulario":formulario}
    return render(request,"appfinal/recomendadores_form.html",contexto)
def alta_recomendadores(request):
    if request.method=="POST":
        formulario=RecomendadorForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            recomendador=Recomendadores(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],itrecruiter=data["itrecruiter"])
            recomendador.save()
            return render(request,"appfinal/index.html")
        pass 
    else:
        formulario = RecomendadorForm()
    contexto = {"formulario":formulario}
    return render(request,"appfinal/recomendadores_form.html")

def alta_clientes(request):
    if request.method=="POST":
        nombre_empresa = request.POST["nombreempresa"]
        desc_empresa = request.POST["descempresa"]
        oferta_activa = request.POST["ofertaactiva"]
        cliente = Clientes(nombreempresa=nombre_empresa,descempresa=desc_empresa,ofertaactiva=oferta_activa)
        cliente.save()
    return render(request,"appfinal/clientes_form.html")

    
def buscar_candidato(request):
    if request.GET:
        candidatos=Candidatos.objects.filter(profesion__icontains=request.GET("profesion"))
        return render(request,"appfinal/busqueda_candidatos.html",{"listado_candidato":candidatos})

    return render(request,"appfinal/busqueda_candidatos.html",{"listado_candidato":[]})


# Create your views here.
# def lista_candidatos(request):
#     candidatos = Candidatos.objects.all()
#     cadena="<ul>"
#     for candidato in Candidatos:
#         cadena+=f"<ul>({candidato.nombre},{candidato.edad})</ul>"
#     cadena+="</ul>"
#     return HttpResponse(cadena)

# def lista_reclutadores(request):
#     reclutadores = Reclutadores.objects.all()
#     cadena="<ul>"
#     for reclutador in Reclutadores:
#         cadena+=f"<ul>({reclutador.nombre})</ul>"
#     cadena+="</ul>"
#     return HttpResponse(cadena)

