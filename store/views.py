from django.shortcuts import render
from .models import Product
from category.models import Category
from .forms import ReviewForm

# Create your views here.
def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    print('single product ', single_product)
    
    return render(request, 'product_details.html', {'product' : single_product})

def write_review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'review.html',{'form':form})
            
    
    