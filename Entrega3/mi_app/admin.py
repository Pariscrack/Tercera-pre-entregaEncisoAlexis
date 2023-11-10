from django.contrib import admin
from .models import Cliente, Proveedor, Pedido

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Pedido)