from django.urls import path
from appfinal.views import *

urlpatterns = [
    path("",inicio,name="tt-inicio"),
    path("candidatos/", candidatos,name="tt-candidatos"),
    path("candidatos/buscar/", profesion_candidato,name="tt-candidatos-buscar"),
    path("candidatos/buscar/resultados/",resultado_candidato,name="tt-candidatos-buscar-resultado"),
    path("recomendadores/",recomendadores,name="tt-recomendadores"),
    path("reclutadores/", reclutadores,name="tt-reclutadores"),
    path("clientes/", clientes,name="tt-clientes"),
    path("candidatos/alta/", alta_candidatos,name="tt-candidatos_form"),
    path("recomendadores/alta/",alta_recomendadores,name="tt-recomendadores_form"),
    path("clientes/alta/", alta_clientes,name="tt-clientes_form"),
]