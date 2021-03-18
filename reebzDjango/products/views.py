from django.shortcuts import render
from . models import product
# Create your views here.


def index(request):
    products = product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/list.html',context)


def detail(request):
    return render(request, 'products/detail.html')


def search(request):
    return render(request, 'products/search.html')