from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OrderItemSerializer,OrderListSerializer
from .models import Order
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes=[TokenAuthentication]
    
    def post(self, request):
        serializer = OrderItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            order_items = serializer.save()
            def calculate_total_price(order_items):
                total_price = 0
                for order_item in order_items:
                    total_price += order_item.cart_item.product.price * order_item.quantity
                return total_price
                
            total_price = calculate_total_price(order_items)
            order, created = Order.objects.get_or_create(user=request.user, total_price=total_price)
            if  created:
                order.order_items.set(order_items)
                return Response({'message': 'Order created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Pending'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class=OrderListSerializer
    permission_classes = [IsAuthenticated] 
    authentication_classes=[TokenAuthentication]
    
    