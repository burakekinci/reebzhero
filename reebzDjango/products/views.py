from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from . models import Product
from . models import SimilarProduct
# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/list.html',context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    similarProducts = SimilarProduct.objects.all()
    context = {
        'product':product,
        'similarProducts':similarProducts,
    }
    return render(request, 'products/detail.html',context)
