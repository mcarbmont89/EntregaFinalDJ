from django import forms

class CandidatoForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    edad = forms.IntegerField()

class RecomendadorForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    itrecruiter = forms.BooleanField()