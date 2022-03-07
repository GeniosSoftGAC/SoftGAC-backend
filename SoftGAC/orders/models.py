from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

from SoftGAC import customers, products



class Orders (models.Model):
    id = models.AutoField(primary_key=True)
    nOrden = models.Random(max_length=4)
    descripcion = models.TextField
    total=models.IntegerField
    cliente = models.ForeignKey(customers, on_delete=CASCADE)
    productos = models.ForeignKey(products, on_delete=CASCADE)
    
