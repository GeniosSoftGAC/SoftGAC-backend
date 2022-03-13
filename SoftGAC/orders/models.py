from unittest.util import _MAX_LENGTH
from django.db import models
from pkg_resources import compatible_platforms

from products.models import Product

class Order (models.Model):
    id = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField
    total=models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    product= models.ManyToManyField(Product)
    
    class Meta:
        ordering = ['-fecha_creacion',]

    def __str__(self):
        return self.primer_nombre
