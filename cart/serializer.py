from rest_framework import serializers
from .models import Cart, CartItem


from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
        

class CartItemListSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=CartItem
        fields=['product','quantity']
        
    
class CartListSerializer(serializers.ModelSerializer):
    item=CartItemListSerializer(many=True, read_only=True)
    
    class Meta:
        model=Cart
        fields=['id','user','item']
    

# Write


        
class CartItemWriteSerializer(serializers.Serializer):
    
    product=serializers.IntegerField(required=True)
    # quantity=serializers.IntegerField(required=True)
    
    


        