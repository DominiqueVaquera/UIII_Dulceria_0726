from django.shortcuts import render, redirect, get_object_or_404
from .models import Dulce, Cliente, Pedido, Empleado, Proveedor, Ingrediente

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

# VISTAS PARA PEDIDOS
def agregar_Pedido(request):
    if request.method == 'POST':
        direccion_envio = request.POST.get('direccion_envio')
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')
        metodo_pago = request.POST.get('metodo_pago')
        dulce_id = request.POST.get('dulce')
        id_pedido = request.POST.get('id_pedido')

        cliente = get_object_or_404(Cliente, id=cliente_id)
        dulce = get_object_or_404(Dulce, id=dulce_id)

        Pedido.objects.create(
            direccion_envio=direccion_envio,
            cliente=cliente,
            estado=estado,
            metodo_pago=metodo_pago,
            dulce=dulce,
            id_pedido=id_pedido
        )
        return redirect('ver_Pedido')
    clientes = Cliente.objects.all()
    dulces = Dulce.objects.all()
    return render(request, 'app_dulces/pedido/agregar_Pedido.html', {'clientes': clientes, 'dulces': dulces})

def ver_Pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'app_dulces/pedido/ver_Pedido.html', {'pedidos': pedidos})

def actualizar_Pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    clientes = Cliente.objects.all()
    dulces = Dulce.objects.all()
    return render(request, 'app_dulces/pedido/actualizar_Pedidos.html', {'pedido': pedido, 'clientes': clientes, 'dulces': dulces})

def realizar_actualizacion_Pedido(request, id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=id)
        pedido.direccion_envio = request.POST.get('direccion_envio')
        cliente_id = request.POST.get('cliente')
        pedido.estado = request.POST.get('estado')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        dulce_id = request.POST.get('dulce')
        pedido.id_pedido = request.POST.get('id_pedido')

        pedido.cliente = get_object_or_404(Cliente, id=cliente_id)
        pedido.dulce = get_object_or_404(Dulce, id=dulce_id)
        pedido.save()
        return redirect('ver_Pedido')

    return redirect('ver_Pedido')

def borrar_Pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'app_dulces/pedido/borrar_Pedido.html', {'pedido': pedido})

def realizar_borrado_Pedido(request, id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=id)
        pedido.delete()
        return redirect('ver_Pedido')

    return redirect('ver_Pedido')

# VISTAS PARA EMPLEADOS
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        puesto = request.POST.get('puesto')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        salario = request.POST.get('salario')

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            puesto=puesto,
            fecha_contratacion=fecha_contratacion,
            salario=salario
        )
        return redirect('ver_empleados')
    return render(request, 'app_dulces/empleado/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'app_dulces/empleado/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'app_dulces/empleado/actualizar_empleado.html', {'empleado': empleado})

def realizar_actualizacion_empleado(request, id):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id=id)
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.email = request.POST.get('email')
        empleado.telefono = request.POST.get('telefono')
        empleado.puesto = request.POST.get('puesto')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado.salario = request.POST.get('salario')
        empleado.save()
        return redirect('ver_empleados')

    return redirect('ver_empleados')

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'app_dulces/empleado/borrar_empleado.html', {'empleado': empleado})

def realizar_borrado_empleado(request, id):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id=id)
        empleado.delete()
        return redirect('ver_empleados')

    return redirect('ver_empleados')

# VISTAS PARA PROVEEDORES
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        Proveedor.objects.create(
            nombre=nombre,
            contacto=contacto,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('ver_proveedores')
    return render(request, 'app_dulces/proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'app_dulces/proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'app_dulces/proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, id):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.nombre = request.POST.get('nombre')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.email = request.POST.get('email')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.save()
        return redirect('ver_proveedores')

    return redirect('ver_proveedores')

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    return render(request, 'app_dulces/proveedor/borrar_proveedor.html', {'proveedor': proveedor})

def realizar_borrado_proveedor(request, id):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, id=id)
        proveedor.delete()
        return redirect('ver_proveedores')

    return redirect('ver_proveedores')

# VISTAS PARA INGREDIENTES
def agregar_ingrediente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        unidad_medida = request.POST.get('unidad_medida')
        stock = request.POST.get('stock')
        precio_unitario = request.POST.get('precio_unitario')
        fecha_caducidad = request.POST.get('fecha_caducidad')
        proveedor_id = request.POST.get('proveedor')

        proveedor = get_object_or_404(Proveedor, id=proveedor_id)

        Ingrediente.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            unidad_medida=unidad_medida,
            stock=stock,
            precio_unitario=precio_unitario,
            fecha_caducidad=fecha_caducidad,
            proveedor=proveedor
        )
        return redirect('ver_ingredientes')
    proveedores = Proveedor.objects.all()
    return render(request, 'app_dulces/ingrediente/agregar_ingrediente.html', {'proveedores': proveedores})

def ver_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'app_dulces/ingrediente/ver_ingredientes.html', {'ingredientes': ingredientes})

def actualizar_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'app_dulces/ingrediente/actualizar_ingrediente.html', {'ingrediente': ingrediente, 'proveedores': proveedores})

def realizar_actualizacion_ingrediente(request, id):
    if request.method == 'POST':
        ingrediente = get_object_or_404(Ingrediente, id=id)
        ingrediente.nombre = request.POST.get('nombre')
        ingrediente.descripcion = request.POST.get('descripcion')
        ingrediente.unidad_medida = request.POST.get('unidad_medida')
        ingrediente.stock = request.POST.get('stock')
        ingrediente.precio_unitario = request.POST.get('precio_unitario')
        ingrediente.fecha_caducidad = request.POST.get('fecha_caducidad')
        proveedor_id = request.POST.get('proveedor')
        ingrediente.proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        ingrediente.save()
        return redirect('ver_ingredientes')

    return redirect('ver_ingredientes')

def borrar_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    return render(request, 'app_dulces/ingrediente/borrar_ingrediente.html', {'ingrediente': ingrediente})

def realizar_borrado_ingrediente(request, id):
    if request.method == 'POST':
        ingrediente = get_object_or_404(Ingrediente, id=id)
        ingrediente.delete()
        return redirect('ver_ingredientes')

    return redirect('ver_ingredientes')
