from django.db import models

from products.models import Product
from users.models import User


class Cart(models.Model):
    """
    Модель корзины пользователя. Связи таблицы:

    user: ForeignKey с моделью User
    products: ManyToMany c таблицей CartItem
    """
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
        ordering = ['-id']
        verbose_name = 'Корзина клиента'
        verbose_name_plural = 'Корзины клиентов'

    def get_cart_items(self):
        return self.cartitem_set.prefetch_related('product').all()

    def clear_cart(self):
        return self.get_cart_items().delete()

    @property
    def total_price(self):
        cart_items = self.get_cart_items()
        return sum(
            cart_item.item_total_price for cart_item in cart_items
        )

    @property
    def count(self):
        return self.get_cart_items().count()

    def __str__(self):
        return f'Корзина пользователя: {self.user.username}'


class CartItem(models.Model):
    """
    Модель товаров в корзине пользователя. Связи таблицы:

    cart: ForeignKey с таблицей Cart
    product: ForeignKey с таблицей Product
    """
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
        ordering = ['-id']
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f'Товар: {self.product} в количестве {self.quantity}'

    @property
    def item_total_price(self):
        """Получение итоговой стоимости товара от его количества."""
        return self.quantity * self.product.price
