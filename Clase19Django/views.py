from django.http import HttpResponse
from django.template import loader
from DataDB.models import Familiares

def familiares(self): #shows data but not from DB, sadly D:

    familiar1 = Familiares(nombre="Sebastian", apellido="Vettel", edad="40", fechaNacimiento="1980-05-12")
    familiar2 = Familiares(nombre="Max", apellido="Verstappen", edad="26", fechaNacimiento="1995-05-12")
    familiar3 = Familiares(nombre="Fernando", apellido="Alonso", edad="41", fechaNacimiento="1979-05-12")

    myList = [familiar1, familiar2, familiar3]
    data = {"dataList":myList}
    
    template = loader.get_template("familiares.html")
    document = template.render(data)
    return HttpResponse(document)

def familiaresFromDB(self): #shows data but not from DB, sadly D:
    familiares = Familiares.objects.all() #get data from DBsqlite
  
    data = {'dataListDB': familiares}

    template = loader.get_template('familiaresFromDB.html')
    document = template.render(data)    
    return HttpResponse(document)

def addFamiliar(self): #if call this from url, add familiars to the db table
    #before save the values showed below, its necessary add the table "Familiares"(from models.py) to the database, for that we need to execute this in a terminal:
    #previous to execute the nexts commands in terminal, check> the syntax in view,urls & models .py are correctly
    #now: 
    #python manage.py makemigrations
    #python manage.py sqlmigrate AppCoder 0001
    #python manage.py migrate

    familiar1 = Familiares(nombre="Sebastian", apellido="Vettel", edad="40", fechaNacimiento="1980-05-12")
    familiar2 = Familiares(nombre="Max", apellido="Verstappen", edad="26", fechaNacimiento="1995-05-12")
    familiar3 = Familiares(nombre="Fernando", apellido="Alonso", edad="41", fechaNacimiento="1979-05-12")

    myList = [familiar1, familiar2, familiar3]

    for n in myList:
        n.save()

    return HttpResponse("Se agregaron los 3 familiares especificados")