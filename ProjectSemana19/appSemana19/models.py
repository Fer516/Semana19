from django.db import models
from django.contrib.auth.models import  Group

Group.objects.get_or_create(name='Cajera')
Group.objects.get_or_create(name='Estudiante')

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveBigIntegerField()
    fk_prov =  models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre