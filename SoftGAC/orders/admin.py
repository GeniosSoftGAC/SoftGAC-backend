from django.contrib import admin
from.models import products
from.models import custumers


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
  list_display: order[
    'nOrden', 
    'descripcion',
    'total'  
  ]



