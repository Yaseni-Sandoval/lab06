from django.shortcuts import get_object_or_404, render

from tienda.models import Categoria, Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.all()
    context = {'product_list': product_list, 'categorias': categorias, 'detalle':True}
    return render(request,'index.html', context)

def producto (request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias = Categoria.objects.all()
    context = {'producto': producto, 'categorias': categorias, 'detalle': True}
    return render(request, 'producto.html', context)

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'productos_por_categoria.html', {'categoria': categoria, 'productos': productos})