# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from shop.models import Product, CartItem

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def sign(request):
    return render(request, 'sign-in.html')

def download_cv(request):
    file_path = "C:\\Users\\sidsa_irhzlmw\\OneDrive\\Desktop\\js e -commerce\\ecomweb\\ecomweb\\doc\\Shivansh cv.pdf"
    try:
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
            return response
    except FileNotFoundError:
        return HttpResponse("CV file not found.", status=404)

