from django.contrib import admin
from .models import Dulce, Cliente

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
