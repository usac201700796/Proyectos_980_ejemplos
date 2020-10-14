from django.db import models

# Create your models here.
"""Para agregar datos a estas bases de Datos usamos el comando
   Ubuntu 
   python3 manage.py shell
   Windows 
   python manege.py shell
   from gestionpedidos.models import Articulos
   Clientes(nombre='', ....)
"""
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=7)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    """ Buscamos en las tablas de la Base de Datos con el siguiente comando
        Articulos.objects.filter(seccion='Dama')
        Rango de Valores
        Mayor que 
        Articulos.objects.filter(secion='Dama',precio__gte=100)
        Menor que 
        Articulos.objects.filter(secion='Dama',precio__lte=100)
        ordenar
        Articulos.objects.filter(precio__gte=50)
        Articulos.objects.filter(precio__gte=50).order_by('precio')
    """
    def __str__(self):
        return 'El nombre del articulo es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)
    

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

