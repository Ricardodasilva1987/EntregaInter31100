
from django.http import HttpResponse
from django.template import Context
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Context,Template,loader
from django.shortcuts import render
from .models import *
from .forms import *

def miprimersaludo(request):
    return HttpResponse("hola es mi primer view")

def probandotemplate(request):
    mihtml = open("C:/Users/rdasilva/Desktop/Django31100/ProyectoFinal/plantilla/template.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

def inicio(request):
    return render(request,"AppProyectoFinal/inicio.html")




def formularioinicio(request):

    if request.method=="POST":
        miFormulario = AmigosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            nombre= info.get("nombre")
            raza = info.get("raza")
            dni = info.get("dni")
            duenio = info.get("duenio")

            amigo=Amigo(nombre=nombre, raza=raza, dni=dni,duenio=duenio) 
            amigo.save()
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'Amigo Creado'})
        else:
            return render(request,"AppProyectoFinal/inico.html",{'mensaje':'error de creacion'})
    else:
        miFormulario=AmigosFormulario()
        return render(request,"AppProyectoFinal/amigos.html",{"formulario":miFormulario})

def juguetes(request):

    if request.method=="POST":
        miFormulariojuguete = JuguetesFormulario(request.POST)
        print(miFormulariojuguete)
        if miFormulariojuguete.is_valid():
            info = miFormulariojuguete.cleaned_data
            nombre= info["nombre"]
            tipo = info["tipo"]
            categoria =info["categoria"]
           

            toy=Juguete(nombre=nombre, tipo=tipo,categoria=categoria) 
            toy.save()
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'Juguete Creado'})
        else:
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'error de creacion'})
    else:
        miFormulariojuguete=JuguetesFormulario()
        return render(request,"AppProyectoFinal/juguetes.html",{"formulario":miFormulariojuguete})
        #return render(request,"AppProyectoFinal/formularioinicio.html",{"formulario":miFormulariojuguete})

def lugares(request):

    if request.method=="POST":
        miFormularioLugar = LugaresFormulario(request.POST)
        print(miFormularioLugar)
        if miFormularioLugar.is_valid():
            info = miFormularioLugar.cleaned_data
            nombre= info["nombre"]
            horario = info["horario"]
            direccion =info["direccion"]
           

            sitio=Lugar(nombre=nombre, horario=horario,direccion=direccion) 
            sitio.save()
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'Lugar Creado'})
        else:
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'error de creacion'})
    else:
        miFormularioLugar=LugaresFormulario()
        return render(request,"AppProyectoFinal/lugares.html",{"formulario":miFormularioLugar})


def comida(request):

    if request.method=="POST":
        miFormularioComida = ComidaFormulario(request.POST)
        print(miFormularioComida)
        if miFormularioComida.is_valid():
            info = miFormularioComida.cleaned_data
            nombre= info["nombre"]
            calorias = info["calorias"]
            recomendable =info["recomendable"]
           

            alimento=Comida(nombre=nombre, calorias=calorias,recomendable=recomendable) 
            alimento.save()
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'Comida Creada'})
        else:
            return render(request,"AppProyectoFinal/inicio.html",{'mensaje':'error de creacion'})
    else:
        miFormularioComida=ComidaFormulario()
        return render(request,"AppProyectoFinal/comida.html",{"formulario":miFormularioComida})



def busquedaDni(request):
    return render(request,"AppProyectoFinal/busquedadni.html")

def buscar(request):
    dni = request.GET["dni"]
    amigos=Amigo.objects.filter(dni=dni)
    if len(amigos) !=0:
        return render(request,"AppProyectoFinal/resultadobusqueda.html",{"amigos":amigos})
    else:
        return render(request,"AppProyectoFinal/resultadobusqueda.html",{"mensaje":"No hay DNI"})
    
#ver amigos en un html

def leerAmigos(request):

    amiguitos = Amigo.objects.all()
    return render(request,"AppProyectoFinal/leerAmigos.html",{"Amiguitos":amiguitos})

#Eliminar amigos
def eliminarAmigos(request, id):
    pet = Amigo.objects.get(id=id)
    pet.delete()
    amiguitos = Amigo.objects.all()
    return render(request,"AppProyectoFinal/leerAmigos.html",{"Amiguitos":amiguitos})

#editar amigos

def editarAmigos(request,id):

    amigo = Amigo.objects.get(id=id)
    if request.method=="POST":
        form=AmigosFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            amigo.nombre= info["nombre"]
            amigo.raza = info["raza"]
            amigo.dni = info["dni"]
            amigo.duenio = info["duenio"]
            amigo.save()
            amiguitos = Amigo.objects.all()
            return render(request,"AppProyectoFinal/leerAmigos.html",{"Amiguitos":amiguitos})
    else:
        form =AmigosFormulario(initial={"nombre":amigo.nombre,"raza":amigo.raza,"dni":amigo.dni,"duenio":amigo.duenio})
        return render(request,"AppProyectoFinal/editarAmigo.html",{"formulario":form, "nombre_amigo":amigo.nombre ,"Id":amigo.id})

                


    

    