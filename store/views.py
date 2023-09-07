from django.shortcuts import render
from .models import Product
from category.models import Category

# Create your views here.
def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    print('single product ', single_product)
    
    return render(request, 'product_details.html', {'product' : single_product})