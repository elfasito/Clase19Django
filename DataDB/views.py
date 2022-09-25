from django.shortcuts import render, redirect
from django.http import HttpResponse
from DataDB.models import Familiares, Mesa
from DataDB.forms import *
from django.contrib.auth.decorators import login_required #especifica que paginas pueden ser accedidas sin login

#libraries for login/logout functions
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def familiares(request):
    if request.method == "POST":
        familiar = Familiares(nombre = request.POST["nombre"], apellido = request.POST["apellido"], edad = request.POST["edad"], fechaNacimiento = request.POST["fecha nacimiento"])
        familiar.save()
        return render(request, "home.html") #nos lleva a home

    return render(request, "familiares.html")

def buscar_familiares(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        familiar = Familiares.objects.filter(nombre__icontains= nombre)
        return render(request, "familiares.html", {'familiares_busqueda': familiar}) #'familiares_busqueda' its the var to use in the template for search
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

def buscar_familiares2(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        familiar = Familiares.objects.filter(nombre__icontains= nombre)
        return render(request, "familiaresCRUD/read_familiares.html", {'familiares_busqueda': familiar}) #'familiares_busqueda' its the var to use in the template for search
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

def create_familiar(request): #its the same what def familiares(request): function ---- but for keep order, create again with the others CRUD functions
    if request.method == "POST":
        familiar = Familiares(nombre = request.POST["nombre"], apellido = request.POST["apellido"], edad = request.POST["edad"], fechaNacimiento = request.POST["fecha nacimiento"])
        familiar.save()

        #this read the data in Familiares DB, and later come back to the link: read_familiares.html to show the last added familiar
        familiares = Familiares.objects.all() #get all data in familiares DB
        return render(request, "familiaresCRUD/read_familiares.html", {'familiares': familiares}) #'familiares' its the var to use in the template for search

    return render(request, "familiaresCRUD/create_familiar.html") 

@login_required #necesita estar logeado para acceder a esta funcion, si no, nos enviará a la pagina de login debido a la configuracion que hicimos en settings.py
def read_familiares(request): 
    familiares = Familiares.objects.all() #get all data in familiares DB
    return render(request, "familiaresCRUD/read_familiares.html", {'familiares': familiares}) #'familiares' its the var to use in the template for search
    
def delete_familiar(request, familiar_idDB): 
    familiar = Familiares.objects.get(id = familiar_idDB) #can use (nombre = familiar_nombre), but if I have multiple familiares in the db with the same name I will get a error, so instead of that I use "id" what is a hidden object parameter in the db
    familiar.delete()

    #this read the data in Familiares DB, and later come back to the link: read_familiares.html to show the last added familiar
    familiares = Familiares.objects.all() #get all data in familiares DB
    return render(request, "familiaresCRUD/read_familiares.html", {'familiares': familiares}) #'familiares' its the var to use in the template for search

def update_familiar(request, familiar_idDB): 
    familiar = Familiares.objects.get(id = familiar_idDB)

    if request.method == "POST":
        formulario =form_familiares(request.POST) #get form_familiares from forms.py

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            familiar.nombre = informacion["nombre"]    
            familiar.apellido = informacion["apellido"] 
            familiar.edad = informacion["edad"] 
            familiar.fechaNacimiento = informacion["fechaNacimiento"] 
            familiar.save()
            familiares = Familiares.objects.all()
            return render(request, "familiaresCRUD/read_familiares.html", {'familiares': familiares})
    else:
        formulario = form_familiares(initial={"nombre": familiar.nombre,"apellido": familiar.apellido,"edad": familiar.edad,"fechaNacimiento": familiar.fechaNacimiento})
    return render(request, "familiaresCRUD/update_familiar.html", {"formulario": formulario})

def api_familiares(request):
    if request.method == "POST":
        formulario = form_familiares(request.POST)
        #print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data           
            familiar = Familiares(nombre= informacion['nombre'], apellido= informacion['apellido'], edad= informacion['edad'], fechaNacimiento= informacion['fecha nacimiento'])
            familiar.save()
            return render(request, "api_familiares.html")
    else:
            formulario = form_familiares()    
    return render(request, "api_familiares.html", {"formulario": formulario})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pw = form.cleaned_data.get("password")

            user = authenticate(username = user, password = pw)

            if user is not None: #si el usuario tiene data (diferente de None)
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {"form":form}) #si falla el logeo, te muestra nuevamente los input para iniciar sesion
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def sign_in(request): #register
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST) #its inherited from forms.py 
        if form.is_valid():
            #user = form.cleaned_data.get("username")
            form.save()
            return redirect("/DataDB/login/")
    else:
        #form = UserCreationForm()
        form = UserRegisterForm() #its inherited from 
        return render(request, "registro.html", {"form": form})
    
def mesas(request):
    if request.method == "POST":
        mesa = Mesa(nombre=request.POST['nombre'], material=request.POST['material'],tipo=request.POST['tipo'],precio=request.POST['precio'])
        mesa.save()
        return render(request, "home.html") #nos lleva a home
    return render(request, "mesas.html")

