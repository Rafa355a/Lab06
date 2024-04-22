from django.urls import path
from . import views 

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    # Nueva ruta para servir imágenes de productos
    path('productos/<str:nombre_imagen>/', views.serve_product_image, name='serve_product_image'),
]
