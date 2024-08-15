from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Cart, CartItem, Product
from .validations import check_correct_qty


class CartService:

    @staticmethod
    def get_user_cart(user: User):
        cart, _ = Cart.objects.get_or_create(
            user=user,
        )
        return cart

    @staticmethod
    def add_to_user_cart(
        user: User, product_id: int, quantity: int,
    ):
        cart, _ = Cart.objects.get_or_create(
            user=user,
        )
        product = get_object_or_404(
            Product, id=product_id
        )
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        updated_quantity = check_correct_qty(
            cart_item=cart_item, created=created, quantity=quantity,
        )

        cart_item.quantity = updated_quantity
        cart_item.save()

        return True

    @staticmethod
    def delete_user_cart_item(
        user: User, product_id: int,
    ):
        cart_item = CartItem.objects.get(
            cart=get_object_or_404(Cart, user=user),
            product=get_object_or_404(Product, id=product_id)
        )
        cart_item.delete()
