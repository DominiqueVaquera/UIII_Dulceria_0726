from django.db import models

class Dulce(models.Model):
    nombre = models.CharField(max_length=150, help_text="Nombre del dulce")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción detallada del dulce")
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del dulce")
    stock = models.PositiveIntegerField(help_text="Cantidad de unidades en stock")
    categoria = models.CharField(max_length=50, help_text="Categoría del dulce (ej. Chocolates, Gomas, Caramelos)")
    fecha_disponibilidad = models.DateField(help_text="Fecha a partir de la cual el dulce está disponible")

    def __str__(self):
        return self.nombre

# ================================== #
# MODELO: CLIENTES
# ==================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
