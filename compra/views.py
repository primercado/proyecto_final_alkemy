from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'compra/agregar_producto.html', {'form': form})

def agregar_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos') 
    else:
        form = ProveedorForm()
    return render(request, 'compra/agregar_proveedor.html', {'form': form})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'compra/listar_proveedores.html', {'proveedores': proveedores})



def inicio(request):
    return render(request, 'compra/inicio.html')
