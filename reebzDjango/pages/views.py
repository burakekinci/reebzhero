from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

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