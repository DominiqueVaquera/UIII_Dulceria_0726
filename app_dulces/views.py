from django.shortcuts import render, redirect, get_object_or_404
from .models import Dulce

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