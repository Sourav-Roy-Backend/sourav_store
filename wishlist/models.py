from django.db import models
from django.contrib.auth.models import User 
from store.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length = 250, blank = True, null=True)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return str(self.product)
    

 
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
