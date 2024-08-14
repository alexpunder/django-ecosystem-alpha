from rest_framework import serializers

from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity',)


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = CartItemSerializer(
        source='cartitem_set',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Cart
        fields = ('user', 'products',)
