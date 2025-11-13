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

# ==========================================
# MODELO: Pedido
# ==========================================
class Pedido(models.Model):
    direccion_envio = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=30)
    metodo_pago = models.CharField(max_length=30)
    dulce = models.ForeignKey(Dulce, on_delete=models.CASCADE)
    id_pedido = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} - {self.cliente.nombre}"

# ================================== #
# MODELO: EMPLEADO
# ==================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    puesto = models.CharField(max_length=100, help_text="Puesto del empleado (ej. Cajero, Repartidor)")
    fecha_contratacion = models.DateField(help_text="Fecha de contratación")
    salario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salario del empleado")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ================================== #
# MODELO: PROVEEDOR
# ==================================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# ================================== #
# MODELO: INGREDIENTE
# ==================================
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=150, help_text="Nombre del ingrediente")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción detallada del ingrediente")
    unidad_medida = models.CharField(max_length=50, help_text="Unidad de medida (ej. kg, litros, unidades)")
    stock = models.PositiveIntegerField(help_text="Cantidad en stock")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio por unidad")
    fecha_caducidad = models.DateField(blank=True, null=True, help_text="Fecha de caducidad")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, help_text="Proveedor del ingrediente")

    def __str__(self):
        return self.nombre
