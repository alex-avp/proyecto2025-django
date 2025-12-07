from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def producto_lista(request):
    productos = Producto.objects.all().order_by('-creado')
    return render(request, 'productos/producto_lista.html', {'productos': productos})

def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Crear producto'})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Editar producto'})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_lista')
    return render(request, 'productos/producto_confirmar_eliminar.html', {'producto': producto})
