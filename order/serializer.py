
from rest_framework import serializers
from .models import OrderItem,Order
from cart.serializer import CartItemListSerializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['cart_item', 'quantity']
        

class OrderListSerializer(serializers.ModelSerializer):
    order_items=OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['order_items', 'total_price']