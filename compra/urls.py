from django.urls import path
from .views import inicio, listar_productos, agregar_producto, listar_proveedores, agregar_proveedor

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', listar_productos, name='listar_productos'),
    path('producto/agregar/', agregar_producto, name='agregar_producto'),
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedor/agregar/', agregar_proveedor, name='agregar_proveedor'),
]
