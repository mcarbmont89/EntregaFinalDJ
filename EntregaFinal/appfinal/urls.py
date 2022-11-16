from django.urls import path
from appfinal.views import *

urlpatterns = [
    path("",inicio),
    path("candidatos/", candidatos),
    path("recomendadores/",recomendadores),
    path("reclutadores/", reclutadores),
    path("clientes/", clientes),
]