from django.urls import path
# Importamos las vistas
from . import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/<int:id>', views.OrdersList.as_view()),  
]