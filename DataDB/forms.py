from django import forms

class form_familiares(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()