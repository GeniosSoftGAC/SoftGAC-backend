from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    primer_nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    direccion = serializers.CharField(max_length=100)
    ciudad = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=100)
    total= serializers.DecimalField(max_digits=8, decimal_places=2)
    product = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    ) 
    
    def create(self, validated_data):
        return Order.objects.create(
            primer_nombre=validated_data.get('primer_nombre'),
            apellido=validated_data.get('apellido'),
            email=validated_data.get('email'),
            direccion=validated_data.get('direccion'),
            telefono=validated_data.get('telefono'),
            ciudad=validated_data.get('ciudad'),
            total=validated_data.get('total'),
            product=validated_data.get('product'),
        )
    
    def update(self, instance, validated_data):
        fields = [
            'primer_nombre',
            'apellido',
            'email',
            'direccion',
            'telefono',
            'ciudad',
            'total',
            'product'
        ]
        
        for field in fields:
            instance[field] = validated_data.get(field, instance.field)
            instance.save()
        
        return instance
    
    class Meta:
        model = Order
        fields = [
            'primer_nombre',
            'apellido',
            'email',
            'direccion',
            'telefono',
            'ciudad',
            'total',
            'product'
        ]
    