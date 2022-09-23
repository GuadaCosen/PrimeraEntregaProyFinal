from pipes import Template
from django.template import Template, Context
from django.http import HttpResponse


def presentacion(request):

    return HttpResponse("Hola a todos!")

def template(request):

    nombre = "Guadalupe"

    pais = "Argentina"

    diccionario = {"name":nombre, "country":pais}

    miHtml = open("C:/Users/tlrte/OneDrive/One Drive/OneDrive/Desktop/1- Proy Final/Proyecto2/Proyecto2/plantillas/plantilla2.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)