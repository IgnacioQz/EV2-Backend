from django.db import models

# Create your models here.

class Producto(models.Model):
    nombreProducto  = models.CharField(max_length=100)
    categoria       = models.CharField(max_length=50, null = True)
    precio          = models.IntegerField()
    stock           = models.IntegerField()
    descripcion     = models.TextField()
    imagen          = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreProducto
