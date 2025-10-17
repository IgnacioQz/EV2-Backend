from django.shortcuts import render
from .models import Producto

# Create your views here.

# Vista para la página de inicio
def home(request):
    context = {}
    productos = Producto.objects.all()
    context['productos'] = productos
    return render(request, 'home.html',context) 

# Vista para el detalle de un producto específico
def producto_detalle(request,id):
    context = {}
    productos = Producto.objects.get(id=id)    
    context["productos"] = productos
    return render(request,"producto_detalle.html", context)

# Vista para la página de categorías
def categoria(request, categoria):
    context = {}
    productos = Producto.objects.filter(categoria=categoria) 
    context['productos'] = productos 
    context['categoria'] = categoria 
    return render(request, 'categoria.html', context)
