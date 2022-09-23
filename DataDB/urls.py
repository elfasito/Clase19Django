from django.urls import path
from DataDB.views import *
from DataDB.forms import *

urlpatterns = [
    path('', home), #if I dont specify a page, it will go automatically to home    
    path('home/', home), #go home when I press button home
    path('index/', index),
    path('familiares/', familiares), #if you append an slash at the end example: 'familiares/', you will need to add the slash too in the action for post data
    path('buscar_familiares/', buscar_familiares),
    path('api_familiares/', api_familiares),
    path('create_familiar/', create_familiar),
    path('delete_familiar/<familiar_idDB>', delete_familiar),
    path('update_familiar/<familiar_idDB>', update_familiar),
    path('read_familiares/', read_familiares),
    path('mesas/', mesas)
]