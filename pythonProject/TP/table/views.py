from django.shortcuts import render
from .models import Product

def home_page(request):
    allobjects = Product.objects.all()
    return render(request, 'home_page.html', {'data': allobjects})
