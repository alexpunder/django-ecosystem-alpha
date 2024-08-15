from rest_framework import serializers

from users.serializers import UserSerializer
from products.serializers import CartProductSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели CartItem. Дополнительно имеет поле получения
    итоговой стоимости товара от его количества.
    """
    product = CartProductSerializer(read_only=True)
    item_total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'item_total_price',)

    def get_item_total_price(self, obj):
        """Получение итоговой стоимости товара от его количества."""
        return obj.item_total_price


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Cart. Имеет дополнительные поля:

    cart_items_total_price: получение итоговой стоимости всех товаров корзины
    cart_items_count: получение итогового количества всех единиц товара корзины
    """
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
        """Получение итоговой стоимости всех товара корзины."""
        return obj.total_price

    def get_cart_items_count(self, obj):
        """Получение итогового количества всех товаров корзины."""
        return obj.count
