
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ("url", "id", "nome", "preco", "quantidade")

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
         model = Product
         fields = ("url", "id", "nome", "preco", "quantidade")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "id", "nome", "email")


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "nome", "email")
