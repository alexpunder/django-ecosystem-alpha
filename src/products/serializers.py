from rest_framework import serializers

from .models import Product, Category, Subcategory, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name', 'slug', 'image',
        )


class ShortSubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = (
            'name', 'slug', 'image',
        )


class SubcategorySerializer(ShortSubcategorySerializer):
    category = CategorySerializer(read_only=True)

    class Meta(ShortSubcategorySerializer.Meta):
        model = Subcategory
        fields = ShortSubcategorySerializer.Meta.fields + (
            'category',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = ShortSubcategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'price', 'category', 'subcategory', 'images',
        )


class CartProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = ShortSubcategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'price', 'category', 'subcategory', 'images',
        )
