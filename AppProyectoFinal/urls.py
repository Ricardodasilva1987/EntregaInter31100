from django.urls import path
from .views import *
from .models import *
from .forms import *

urlpatterns = [
    
    path("hola/",miprimersaludo,name="hola"),
    path("html/",probandotemplate, name = "probandotemplate"),
    path("", inicio, name ="inicio"),
    path("lugares/",lugares, name = "lugares"),
    path("amigos/",formularioinicio, name="amigos"),
    path("juguetes/",juguetes, name ="juguetes"),
    path("comida/",comida, name="comida"),
    path("busquedaDni/",busquedaDni,name="busquedadni"),
    path("resultadobusqueda/",buscar,name="buscar"),
    path("leerAmigos/",leerAmigos,name="leerAmigos"),
    path("eliminarAmigo/<id>",eliminarAmigos,name="eliminarAmigo"),
    path("editarAmigo/<id>",editarAmigos,name="editarAmigo"),

]
