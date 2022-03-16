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
    total = serializers.DecimalField(max_digits=8, decimal_places=2)
    products = ProductSerializer(
        many=True
    )

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
            'products'
        ]

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        return Order.objects.create(order=order, **products_data)

    def update(self, instance, validated_data):
        fields = [
            'primer_nombre',
            'apellido',
            'email',
            'direccion',
            'telefono',
            'ciudad',
            'total',
            'products'
        ]

        for field in fields:
            instance[field] = validated_data.get(field, instance.field)
            instance.save()

        return instance
