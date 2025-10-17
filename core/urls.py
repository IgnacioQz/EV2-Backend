from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:id>/', views.detalleProducto, name='producto_detalle'),
    path('categoria/<str:categoria>/', views.categoria, name='categoria'),
]