from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import ProtectedError

from users.models import Product

# ----- VISTAS EXISTENTES -----
def test_view(request):
    return HttpResponse("<h1>¡Hola! Esta es una vista de prueba.</h1>")

def home(request):
    user = request.user
    context = {
        'title': 'Proyecto 2025',
        'message': 'Bienvenido al proyecto de prueba'
    }
    return render(request, 'home.html', context)

def welcome(request):
    return render(request, "base.html")

def about(request):
    context = {
        "products": Product.objects.filter(is_active=True)
    }
    return render(request, "about.html", context=context)

def create_product(request):
    if request.method == "GET":
        return render(request, "product/create.html")
    else:
        product = Product()
        product.name = request.POST['name_product']
        product.stock = request.POST['stock_product']
        # opcional: activo por defecto
        product.save()
        messages.success(request, "Producto creado correctamente.")
        return redirect(reverse_lazy("about"))

# ----- NUEVAS: UPDATE & DELETE -----
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, "product/edit.html", {"product": product})
    else:
        product.name = request.POST.get("name_product", product.name)
        product.stock = request.POST.get("stock_product", product.stock)
        # checkbox: si no viene, es False
        product.is_active = bool(request.POST.get("is_active"))
        product.save()
        messages.success(request, "Producto actualizado.")
        return redirect(reverse_lazy("about"))

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        try:
            product.delete()
            messages.success(request, "Producto eliminado.")
        except ProtectedError:
            messages.error(
                request,
                "No se puede eliminar: tiene registros relacionados (DetailProduct)."
            )
        return redirect(reverse_lazy("about"))
    # GET -> página de confirmación
    return render(request, "product/confirm_delete.html", {"product": product})
