from django import forms


class Formulariosobremi(forms.Form):

    nombre = forms.CharField()
    edad = forms.IntegerField()
    profesion = forms.CharField()


