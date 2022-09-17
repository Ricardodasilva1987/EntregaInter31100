from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Amigo(models.Model):
    nombre =models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    dni = models.IntegerField()
    duenio= models.CharField(max_length=50)

    def __str__(self) :
        return f"NOMBRE: {self.nombre} - RAZA: {self.raza} - DNI: {self.dni} - DUENIO: {self.duenio}"



class Juguete(models.Model):
    nombre =models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=50)
    def __str__(self) :
        return f"NOMBRE: {self.nombre} TIPO: {self.tipo} CATEGORIA: {self.categoria} "
    


class Lugar(models.Model):
    nombre =models.CharField(max_length=30)
    horario = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)

    def __str__(self) :
        return f"NOMBRE: {self.nombre} HORARIO: {self.horario} DIRECCION: {self.direccion} "

class Comida(models.Model):
    nombre=models.CharField(max_length=30)
    calorias = models.IntegerField()
    recomendable = models.BooleanField()

    
    def __str__(self) :
        return f"NOMBRE: {self.nombre} CAL: {self.calorias} Recomendable: {self.recomendable} "


   

