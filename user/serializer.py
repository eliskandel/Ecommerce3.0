from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
    def create(self, validated_data):
        password=validated_data.pop('password')
        user_category=validated_data.get('category')
        if user_category == "seller":
            user=User.objects.create(**validated_data)
        else:
            user=User.objects.create(**validated_data)

        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password']=make_password(validated_data['password'])
        return super().update(instance, validated_data)

class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'first_name',
            'email',
            'caterogy'
            
        ]

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
class UserLogoutSerializer(serializers.Serializer):
    token=serializers.CharField(required=True)