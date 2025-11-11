from django.shortcuts import render, redirect, get_object_or_404
from .models import Dulce, Cliente

def inicio_dulceria(request):
    return render(request, 'app_dulces/inicio.html')

# VISTAS PARA DULCES
def agregar_dulce(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria = request.POST.get('categoria')
        fecha_disponibilidad = request.POST.get('fecha_disponibilidad')

        Dulce.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            fecha_disponibilidad=fecha_disponibilidad
        )
        return redirect('ver_dulces')
    return render(request, 'app_dulces/dulce/agregar_dulce.html')


def ver_dulces(request):
    dulces = Dulce.objects.all()
    return render(request, 'app_dulces/dulce/ver_dulces.html', {'dulces': dulces})

def actualizar_dulce(request, id):
    dulce = get_object_or_404(Dulce, id=id)
    return render(request, 'app_dulces/dulce/actualizar_dulce.html', {'dulce': dulce})

def realizar_actualizacion_dulce(request, id):
    if request.method == 'POST':
        dulce = get_object_or_404(Dulce, id=id)
        dulce.nombre = request.POST.get('nombre')
        dulce.descripcion = request.POST.get('descripcion')
        dulce.precio = request.POST.get('precio')
        dulce.stock = request.POST.get('stock')
        dulce.categoria = request.POST.get('categoria')
        dulce.fecha_disponibilidad = request.POST.get('fecha_disponibilidad')
        dulce.save()
        return redirect('ver_dulces')

    return redirect('ver_dulces')

def borrar_dulce(request, id):
    dulce = get_object_or_404(Dulce, id=id)
    return render(request, 'app_dulces/dulce/borrar_dulce.html', {'dulce': dulce})

def realizar_borrado_dulce(request, id):
    if request.method == 'POST':
        dulce = get_object_or_404(Dulce, id=id)
        dulce.delete()
        return redirect('ver_dulces')

    return redirect('ver_dulces')

# VISTAS PARA CLIENTES
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('ver_clientes')
    return render(request, 'app_dulces/cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_dulces/cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'app_dulces/cliente/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=id)
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('ver_clientes')

    return redirect('ver_clientes')

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'app_dulces/cliente/borrar_cliente.html', {'cliente': cliente})


def realizar_borrado_cliente(request, id):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id=id)
        cliente.delete()
        return redirect('ver_clientes')

    return redirect('ver_clientes')
