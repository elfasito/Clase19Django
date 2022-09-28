from django.urls import path
from DataDB.views import *
from DataDB.forms import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home), #if I dont specify a page, it will go automatically to home    
    path('home/', home), #go home when I press button home
    path('index/', index),
    path('familiares/', familiares), #if you append an slash at the end example: 'familiares/', you will need to add the slash too in the action for post data
    path('buscar_familiares/', buscar_familiares),
    path('buscar_familiares2/', buscar_familiares2),
    path('api_familiares/', api_familiares),
    path('create_familiar/', create_familiar),
    path('delete_familiar/<familiar_idDB>', delete_familiar),
    path('update_familiar/<familiar_idDB>', update_familiar),
    path('read_familiares/', read_familiares),
    path('login/', login_request),
    path('sign_in/', sign_in),
    path('logout/', LogoutView.as_view(template_name = "home.html"), name = "Sesion cerrada"),
    path('editarPerfil/', update_profile),
    path('mesas/', mesas)
]