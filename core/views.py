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

# función de contexto para proporcionar categorías a todas las plantillas
def categorias_context(request):
    categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    return {'categorias': categorias}

# Vista para la página de categorías
def categoria(request):
    return render(request, 'categoria.html')

# Vista para la página de detalle del producto
def detalleProducto(request):
    return render(request, 'detalle.html')