from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import SobreMi
from AppCoder.models import Materia1
from AppCoder.models import Materia2

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def sobremi(request):

    Data_1 = SobreMi(nombre="Guadalupe", edad="23", profesion="Estudio actuario en administracion y trabajo como analista de datos.")
    Data_1.save()

    return render(request, "AppCoder/sobremi.html")

def materia1(request):

    Data_2 = Materia1(nombre="Matematica para economistas", temas="Transformaciones lineales, optimizacion libre y con restricciones", primerparcial= "14/10/2022.")
    Data_2.save()

    return render(request, "AppCoder/materia1.html")

def materia2(request):

    Data_3 = Materia2(nombre="Estadistica 2", temas="Distribuciones, test de hipotesis, estimadores", primerparcial= "17/10/2022")
    Data_3.save()

    return render(request, "AppCoder/materia2.html")

def Formulariosobremi(request):

    if request.method == "POST":

        sobremi = SobreMi(nombre=request.POST["Nombre"], edad=request.POST["Edad"], profesion=request.POST["Profesion"])

        sobremi.save()

        return render(request, "AppCoder/inicio.html")


    return render(request, "AppCoder/Formulariosobremi.html")
        

def busquedaedad(request):

    return render(request, "AppCoder/busquedaedad.html")

def resultados(request):

    if request.GET["edad"]:

        edad = request.GET["edad"]
        nombre = SobreMi.objects.filter(edad__icontains=edad)

        return render(request, "AppCoder/resultados.html", {"nombre":nombre, "edad":edad})

    else:

        respuesta = "No ingresaste datos."


    return HttpResponse(respuesta)


  