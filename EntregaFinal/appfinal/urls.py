from django.urls import path
from appfinal.views import *

urlpatterns = [
    path("",inicio,name="tt-inicio"),
    path("candidatos/", candidatos,name="tt-candidatos"),
    path("recomendadores/",recomendadores,name="tt-recomendadores"),
    path("reclutadores/", reclutadores,name="tt-reclutadores"),
    path("clientes/", clientes,name="tt-clientes"),
]