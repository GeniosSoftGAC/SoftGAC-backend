from rest_framework import serializers
from .models import Orders
from tkinter import CASCADE
from .models import customers
from .models import products

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.AutoField(primary_key=True)
    nOrden = serializers.Random(max_length=4)
    descripcion = serializers.CharField(max_length=1000)
    total= serializers.IntegerField
    cliente = serializers.ForeignKey(customers, on_delete=CASCADE)
    productos = serializers.ForeignKey(products, on_delete=CASCADE)
    
    def create(self, validated_data):
        return super().create(
            nOrden =  validated_data.get('nOrden'),
            descripcion = validated_data.get('descripcion'),
            total = validated_data.get('total'),
            cliente = validated_data.get('cliente'),
            productos = validated_data.get('productos')          
            )