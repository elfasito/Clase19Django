from django.shortcuts import render
from django.http import HttpResponse
from DataDB.models import Familiares, Mesa
from DataDB.forms import *

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

def create_familiar(request): #its the same what def familiares(request): function ---- but for keep order, create again with the others CRUD functions
    if request.method == "POST":
        familiar = Familiares(nombre = request.POST["nombre"], apellido = request.POST["apellido"], edad = request.POST["edad"], fechaNacimiento = request.POST["fecha nacimiento"])
        familiar.save()

        #this read the data in Familiares DB, and later come back to the link: read_familiares.html to show the last added familiar
        familiares = Familiares.objects.all() #get all data in familiares DB
        return render(request, "familiaresCRUD/read_familiares.html", {'familiares': familiares}) #'familiares' its the var to use in the template for search

    return render(request, "familiaresCRUD/create_familiar.html") 

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

def mesas(request):
    if request.method == "POST":
        mesa = Mesa(nombre=request.POST['nombre'], material=request.POST['material'],tipo=request.POST['tipo'],precio=request.POST['precio'])
        mesa.save()
        return render(request, "home.html") #nos lleva a home
    return render(request, "mesas.html")

