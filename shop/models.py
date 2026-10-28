from django.db import models

# Create your models here.


class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def meta():
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    cliente = models.ForeignKey (on_delete=models.CASCADE, to=Cliente, related_name='productos')
    nombre = models.CharField (max_length = 50)
    cantidad = models.IntegerField()
    precio = models.BigIntegerField ()

    def meta():
        ordering = ['nombre']
    
    def __str__ (self):
        return f"{self.nombre} - {self.cliente.nombre}"
    
