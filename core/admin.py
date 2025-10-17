from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto','categoria', 'precio', 'stock', 'descripcion', 'imagen')

admin.site.register(Producto, ProductoAdmin)
