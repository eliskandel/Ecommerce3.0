from rest_framework.response import Response
# Create your views here.
from  .serializer import(
    CartListSerializer,
    CartItemListSerializer,
    CartItemWriteSerializer
)
from rest_framework.generics import(
    ListAPIView,
    GenericAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)
from .models import Cart,CartItem
from product.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CartListView(ListAPIView):
    serializer_class=CartListSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemListView(ListAPIView):
    serializer_class=CartItemListSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user).first()
        return CartItem.objects.filter(cart=cart)

    
class CartItemAddAPIView(CreateAPIView):
    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        user = self.request.user  # Assuming the user is authenticated
        cart, created = Cart.objects.get_or_create(user=user)
        serializer = CartItemWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        product_id = serializer.validated_data['product']
        

        # Check if the product is already in the cart
        cart_item, created = cart.cart_items.get_or_create(product_id=product_id)
        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()

        return Response(serializer.data)

class CartItemRemoveView(DestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self, pk):
        cart=Cart.objects.get(user=self.request.user)
        cart_item=cart.cart_items.get(product_id=pk)
        return cart_item