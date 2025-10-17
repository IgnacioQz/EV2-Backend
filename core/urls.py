from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalle/', views.detalleProducto, name='detalleProducto'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
]