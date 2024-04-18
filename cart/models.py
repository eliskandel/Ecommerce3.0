from django.db import models
from user.models import User
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user}\'s Cart'
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return f'{self.product} Item of {self.cart.user}'