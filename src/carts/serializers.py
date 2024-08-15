from rest_framework import serializers

from users.serializers import UserSerializer
from products.serializers import CartProductSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializer(read_only=True)
    item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'item_total_price',)

    def get_item_total_price(self, obj):
        return obj.item_total_price


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = CartItemSerializer(
        source='cartitem_set',
        many=True,
        read_only=True,
    )
    cart_items_total_price = serializers.SerializerMethodField()
    cart_items_count = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = (
            'user', 'products',
            'cart_items_total_price', 'cart_items_count',
        )

    def get_cart_items_total_price(self, obj):
        return obj.total_price

    def get_cart_items_count(self, obj):
        return obj.count
