from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Cart, CartItem, Product


class CartService:

    @classmethod
    def get_user_cart(user: User):
        return get_object_or_404(Cart, user=user)

    @classmethod
    def add_to_user_cart(
        user: User, product: Product, quantity: int = 1,
    ):
        cart, _ = Cart.objects.get_or_create(
            user=user,
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

    @classmethod
    def delete_user_cart_item(
        user: User, pk: int,
    ):
        cart_item = CartItem.objects.get(
                cart=get_object_or_404(Cart, user=user),
                product=get_object_or_404(Product, pk=pk)
            )
        cart_item.delete()
