from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category


def home(request,category_slug=None):
    
    products =None
    
    if category_slug:
        category = get_object_or_404(Category, slug =category_slug)
        products = Product.objects.filter(is_available = True,category=category)
    else:
        products = Product.objects.filter(is_available = True)
    categories = Category.objects.all()
    
    context = {'products':products,'categories': categories}
    return render(request,'sourav_store/base.html',context)

def orderby(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'sourav_store/base.html', {'products': products})