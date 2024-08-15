from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Cart, CartItem, Product
from .validations import check_correct_qty


class CartService:
    """Методы для работы с корзиной пользователя."""

    @staticmethod
    def get_user_cart(user: User) -> Cart:
        """
        Метод получения пользовательской корзины покупок и создания
        при необходимости новой.

        Принимает в качестве аргументов:
        user: объект модели User

        Возвращает объект модели Cart.
        """
        cart, _ = Cart.objects.get_or_create(
            user=user,
        )
        return cart

    @staticmethod
    def add_to_user_cart(
        user: User, product_id: int, quantity: int,
    ) -> None:
        """
        Метод добавления товара в корзину. По-умолчанию добавляет одну единицу
        товара, если не передан параметр количества.
        Можно передавать отрицательное кличество, но меньше одной единицы
        сделать не получится - возникнет ошибка.

        Принимает в качестве аргументов:
        user: объект модели User
        product_id: уникальный идентификатор товара типа int
        quantity: количество добавляемого/удаляемого товара типа int

        Метод ничего не возвращает.
        """
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

    @staticmethod
    def delete_user_cart_item(
        user: User, product_id: int,
    ) -> None:
        """
        Метод удаления товара из корзины. Сама корзина пользователя при этом
        остается.

        Принимает в качестве аргументов:
        user: объект модели User
        product_id: уникальный идентификатор товара типа int

        Метод ничего не возвращает.
        """
        cart_item = CartItem.objects.get(
            cart=get_object_or_404(Cart, user=user),
            product=get_object_or_404(Product, id=product_id)
        )
        cart_item.delete()
