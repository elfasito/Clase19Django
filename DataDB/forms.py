from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_familiares(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()

class UserRegisterForm(UserCreationForm): #basicamente agarra el form original de django(UserCreationForm) y lo personalizo con fields nuevos
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}
