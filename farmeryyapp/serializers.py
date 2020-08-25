from rest_framework import serializers
from farmeryyapp.models import Info,Product,Category1,ProductType,Product2,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields=['id','first_name','last_name','email','phno','refphno','user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={"password":{"write_only":True,'required':True}}
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields= '__all__'

class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model=Category1
        fields= '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProductType
        fields= '__all__'


class Product2Serializer(serializers.ModelSerializer):

    class Meta:
        model=Product2
        fields= '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rating
        fields= '__all__'
