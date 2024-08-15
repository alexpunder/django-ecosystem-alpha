from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Cart, CartItem, Product


class CartService:

    @staticmethod
    def get_user_cart(user: User):
        return get_object_or_404(Cart, user=user)

    @staticmethod
    def add_to_user_cart(
        user: User, product_id: int, quantity: int = 1,
    ):
        cart, _ = Cart.objects.get_or_create(
            user=user,
        )
        product = get_object_or_404(
            Product, id=product_id
        )
        cart_product, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        if not created:
            updated_quantity = cart_product.quantity + quantity
            cart_product.quantity = updated_quantity
            cart_product.save()
        else:
            cart_product.quantity = quantity
            cart_product.save()

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
