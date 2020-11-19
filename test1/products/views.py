from django.http import JsonResponse
from .models import Product, Manufacturer




def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    #data = {"products": list(products.values("pk", "name"))}
    data = {"manufacturers": list(manufacturers.values())}

    response = JsonResponse(data)

    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_products.values())
            }
        }
        status_code = 200
    except Product.DoesNotExist:
        data = {
            "error": {
                "code": 404,
                "message": "product not found"
            }
        }
        status_code = 404

    response = JsonResponse(data, status=status_code)
    return response

def product_list(request):
    products = Product.objects.all()
    #data = {"products": list(products.values("pk", "name"))}
    data = {"products": list(products.values())}

    response = JsonResponse(data)

    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity
            }
        }
        status_code = 200
    except Product.DoesNotExist:
        data = {
            "error": {
                "code": 404,
                "message": "product not found"
            }
        }
        status_code = 404

    response = JsonResponse(data, status=status_code)
    return response






#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView
#
#from .models import Product, Manufacturer
#
#
#class ProductDetailView(DetailView):
#    model = Product
#    template_name = "products/product_detail.html"
#
#class ProductListView(ListView):
#    model = Product
#    template_name = "products/product_list.html"
#
