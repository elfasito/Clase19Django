from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()

    #hecho en clase 22, si entro en administracion y a la tabla de familiares, ahora me muestra directamente los datos guardados, en vez de tener que entrar al object y ver que data tiene dentro.
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Edad:{self.edad} - Fecha nacimiento:{self.fechaNacimiento}"

class Mesa(models.Model):
    nombre = models.CharField(max_length= 30)
    material = models.CharField(max_length= 30)
    tipo= models.CharField(max_length= 30)
    precio = models.IntegerField()