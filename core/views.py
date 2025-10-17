from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    context = {}

    productos = Producto.objects.all()
    context['productos'] = productos

    return render(request, 'home.html',context)

def producto_detalle(request,id):
    
    context = {}
    
    productos = Producto.objects.get(id=id)    
    context["productos"] = productos
    return render(request,"producto_detalle.html", context)

def categoria(request):
    return render(request, 'categoria.html')

def detalleProducto(request):
    return render(request, 'detalle.html')