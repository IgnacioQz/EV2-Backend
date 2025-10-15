from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('categoria/', views.categoria, name='categoria'),
    path('detalle/', views.detalleProducto, name='detalleProducto'),
]