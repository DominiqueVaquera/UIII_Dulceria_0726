from django.contrib import admin
from .models import Dulce

@admin.register(Dulce)
class DulceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fecha_disponibilidad')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')