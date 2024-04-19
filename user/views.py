from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)
from .models import User
from .serializer import (
    UserSerializer,
    UserRetriveSerializer,
    UserLoginSerializer,
    UserLogoutSerializer
    
    )
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserListView(ListAPIView):
    queryset=User.objects.all()
    serializer_class= UserRetriveSerializer
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    
class UserRetrieveView(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserRetriveSerializer 
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return User.objects.filter(id=pk)
    
class UserLoginView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer= UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username=serializer.validated_data.get('username')
        password=serializer.validated_data.get('password')
        
        
        try:
            user= User.objects.get(username=username)
        except:
            return Response({"message":"Invalid Credentials"},status=401)
        
        if not user.check_password(password):
            return Response({"message":"Invalid Credentials"},status=401)
        token, create=Token.objects.get_or_create(user=user)
        
        return Response({"message":"Login Successful","token":token.key})
    
    
class UserLogoutView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer=UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_token= serializer.validated_data.get('token')
        
        try: 
            token=Token.objects.get(key=user_token)
            token.delete()
            return Response({"message":"Logout Successful"})

        except:
            return Response({"message":"Invalid Credentials"},status=401)

class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer
    
    
    
class UserDeleteView(DestroyAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
    
class UserUpdateView(UpdateAPIView):
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
         
    