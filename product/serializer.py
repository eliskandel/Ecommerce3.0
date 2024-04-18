from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','description','price']
        
    def create(self, validated_data):
        request=self.context['request']
        
        if request.user.caterogy == "seller":
            product=Product.objects.create(**validated_data,seller=request.user)
            return product
        else:
            raise serializers.ValidationError("Category does not meet requirement")
    
    