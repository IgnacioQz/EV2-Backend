# mi_app/context_processors.py
from .models import Producto

def categorias_context(request):
    categorias = Producto.objects.values_list('categoria', flat=True).distinct()
    return {'categorias': categorias}