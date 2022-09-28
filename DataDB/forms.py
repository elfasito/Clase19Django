from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "Username"}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': "Email"}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "First name"}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "Last name"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': "Password"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        help_texts = {k: "" for k in fields}
