from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def categoria(request):
    return render(request, 'categoria.html')

def detalleProducto(request):
    return render(request, 'detalle.html')