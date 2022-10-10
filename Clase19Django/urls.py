from pydoc import doc
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include #manually added the include
from Clase19Django.views import familiares, familiaresFromDB, addFamiliar, mainhome #manual import

urlpatterns = [
    path('', mainhome),
    path('admin/', admin.site.urls),
    path('familiares/', familiares),
    path('addFamiliar/', addFamiliar),
    path('familiaresFromDB/', familiaresFromDB),
    path('DataDB/', include("DataDB.urls")) #include the functions from the secondary app urls.py file
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #agrega carpeta media al directorio