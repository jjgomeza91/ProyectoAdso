from django.shortcuts import render


def principal(request):
    titulo="Bienvenido"
    context={
        "titulo": titulo
    }
    return render(request, "index.html", context)

def clientes(request):
    titulo="Clientes"
    context={
        "titulo": titulo
    }
    return render(request, "clientes.html", context)

def ventas(request):
    titulo="Ventas"
    context={
        "titulo": titulo
    }
    return render(request, "ventas.html", context)

def devoluciones(request):
    titulo="Devoluciones"
    context={
        "titulo": titulo
    }
    return render(request, "devoluciones.html", context)

def bodegas(request):
    titulo="Bodegas"
    context={
        "titulo": titulo
    }
    return render(request, "bodegas.html", context)

def compras(request):
    titulo="Compras"
    context={
        "titulo": titulo
    }
    return render(request, "compras.html", context)

def productos(request):
    titulo="Productos"
    context={
        "titulo": titulo
    }
    return render(request, "productos.html", context)

def proveedores(request):
    titulo="Proveedores"
    context={
        "titulo": titulo
    }
    return render(request, "proveedores.html", context)

def roles(request):
    titulo="Roles"
    context={
        "titulo": titulo
    }
    return render(request, "roles.html", context)

def usuarios(request):
    titulo="Usuarios"
    context={
        "titulo": titulo
    }
    return render(request, "usuarios.html", context)