from django.contrib import admin
from .models import Dulce, Cliente, Pedido

@admin.register(Dulce)
class DulceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fecha_disponibilidad')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_registro')
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'cliente', 'dulce', 'estado', 'metodo_pago', 'fecha_pedido')
    list_filter = ('estado', 'fecha_pedido')
    search_fields = ('id_pedido', 'cliente__nombre', 'dulce__nombre')
