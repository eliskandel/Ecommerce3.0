from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OrderItemSerializer
from .models import Order
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes=[TokenAuthentication]
    def calculate_total_price(order_items):
        pass
    def post(self, request):
        serializer = OrderItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            order_items = serializer.save()
            # Assuming you have a method to calculate the total price of the order
            total_price = 100
            order, created = Order.objects.get_or_create(user=request.user, total_price=total_price)
            if  created:
                order.order_items.set(order_items)
                return Response({'message': 'Order created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Pending'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        