from django.shortcuts import render
from django.http import HttpResponse
from . models import mainPageProduct
# Create your views here.

def index(request):
    mainPageProducts = mainPageProduct.objects.all()
    context = {
        'mainPageProducts': mainPageProducts
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def contract(request):
    return render(request, 'pages/contract.html')

def sss(request):
    return render(request, 'pages/sss.html')

def privacy(request):
    return render(request, 'pages/privacy.html')    