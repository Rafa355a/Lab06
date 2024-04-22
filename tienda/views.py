from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Producto

def index(request):
    product_list = Producto.objects.all()
    context = {'product_list': product_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {"producto": producto})

def serve_product_image(request, nombre_imagen):
    producto = get_object_or_404(Producto, imagen=nombre_imagen)

    with open(producto.imagen.path, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')  
