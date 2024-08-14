from django.db import models

from products.models import Product
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
    )
    products = models.ManyToManyField(
        Product,
        through='CartItem',
        verbose_name='Товары'
    )

    class Meta:
        verbose_name = 'Корзина клиента'
        verbose_name_plural = 'Корзины клиентов'

    def __str__(self):
        return f'Корзина пользователя: {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        verbose_name='Корзина',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество единиц товара'
    )

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
