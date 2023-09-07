from django.shortcuts import render, redirect
from store.models import Product
# Create your views here.
from .models import Cart, CartItem
def cart(request):
    session_id = request.session.session_key
    cartid,created = Cart.objects.get_or_create(cart_id = session_id)
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    cart_items =None
    if cart_id:
        cart_items = CartItem.objects.filter(cart=cartid)
    
    return render(request, 'wishlist.html',{'cart_items' : cart_items})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_exists = Cart.objects.filter(cart_id=session_id).exists()
    
    if cart_exists:
        cart = Cart.objects.get(cart_id=session_id)
        cart_item_exists = CartItem.objects.filter(cart=cart, product=product).exists()
        
        if cart_item_exists:
            item = CartItem.objects.get(cart=cart, product=product)
            item.quantity += 1
            item.save()
        else:
            item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        
    else:
        cart = Cart.objects.create(cart_id=session_id)
        item = CartItem.objects.create(cart=cart, product=product, quantity=1)
    
    return redirect('cart')