from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('sobremi/', sobremi, name="Sobremi"),
    path('mate/', materia1, name="Matematica para economistas"),
    path('est2/', materia2, name="Estadistica 2"),
    path('Formulariosobremi/', Formulariosobremi, name="formularioSobremi"),
    path('buscaredad/', busquedaedad, name="BuscarEdad"),
    path('resultados/', resultados, name="ResultadosBusquedas"),
]