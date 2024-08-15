from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from src.constants import (
    NAME_MAX_LENGTH, SLUG_MAX_LENGTH, MAX_DECIMAL_PLACES_PRICE,
    MAX_DIGITS_PRICE, IMAGE_SIZE_MAX_LENGTH,
)


class Base(models.Model):
    name = models.CharField(
        'Название',
        max_length=NAME_MAX_LENGTH,
    )
    slug = models.SlugField(
        'Слаг',
        max_length=SLUG_MAX_LENGTH,
        unique=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(Base):
    price = models.DecimalField(
        'Цена товара',
        max_digits=MAX_DIGITS_PRICE,
        decimal_places=MAX_DECIMAL_PLACES_PRICE,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категории',
    )
    subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Подкатегории',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    class ImageChoices(models.TextChoices):
        LARGE = 'LARGE', _('Большое')
        MEDIUM = 'MEDIUM', _('Среднее')
        SMALL = 'SMALL', _('Маленькое')

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар',
    )
    image = models.ImageField(
        'Изображение товара',
        upload_to='product_images',
    )
    size = models.CharField(
        'Размер изображения',
        max_length=IMAGE_SIZE_MAX_LENGTH,
        choices=ImageChoices.choices,
        default=ImageChoices.LARGE,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f'Изображение для товара: {self.product.name}'


class Category(Base):
    image = models.ImageField(
        'Изображение категории',
        upload_to='categories_image',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(Base):
    image = models.ImageField(
        'Изображение подкатегории',
        upload_to='subcategories_image',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='subcategories',
        verbose_name='Категория'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
