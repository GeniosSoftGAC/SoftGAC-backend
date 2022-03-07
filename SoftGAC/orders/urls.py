from django.urls import path
# Importamos las vistas
from . import views

urlpatterns = [
    # Creamos las rutas para publicar los endpoints
    path('orders/', views.ProductListView.as_view()),
    path('orders/<int:id>', views.ProductListView.as_view()),
]