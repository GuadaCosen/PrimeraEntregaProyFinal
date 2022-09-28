from django.db import models

# Create your models here.

class SobreMi(models.Model):

    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=60)

class Materia1(models.Model):

    nombre = models.CharField(max_length=20)
    temas = models.CharField(max_length=60)
    primerparcial = models.CharField(max_length=20)

class Materia2(models.Model):

    nombre = models.CharField(max_length=30)
    temas = models.CharField(max_length=60)
    primerparcial = models.CharField(max_length=20)

