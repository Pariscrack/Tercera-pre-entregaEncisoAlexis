from django.urls import path
from . import views

urlpatterns = [
    path('crear-cliente/', views.crear_cliente, name='crear-cliente'),
    path('crear-proveedor/', views.crear_proveedor, name='crear-proveedor'),
    path('crear-pedido/', views.crear_pedido, name='crear-pedido'),
    path('buscar/', views.buscar, name='buscar'),
]