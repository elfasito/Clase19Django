from django.contrib import admin
from django.urls import path, include #manually added the include
from Clase19Django.views import familiares, familiaresFromDB, addFamiliar #manual import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiares/', familiares),
    path('addFamiliar/', addFamiliar),
    path('familiaresFromDB/', familiaresFromDB),
    path('DataDB/', include("DataDB.urls")) #include the functions from the secondary app urls.py file
]
