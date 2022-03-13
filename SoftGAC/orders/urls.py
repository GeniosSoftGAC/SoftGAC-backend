from django.urls import path
# Importamos las vistas
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view()),  
    path('orders/<int:id>', views.OrderListView.as_view()),  
]