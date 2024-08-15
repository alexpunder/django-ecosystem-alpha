from django.contrib import admin

from src.constants import MAX_PRODUCT_IMAGES
from .models import Product, ProductImage, Category, Subcategory


class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = MAX_PRODUCT_IMAGES
    max_num = MAX_PRODUCT_IMAGES
    can_delete = True


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    inlines = (ProductImageInline,)
    list_display = (
        'id', 'name', 'slug', 'price', 'category', 'subcategory',
    )
    list_editable = (
        'price', 'category', 'subcategory',
    )
    list_filter = (
        'category', 'subcategory',
    )
    search_fields = (
        'name',
    )


class SubcategoryInLine(admin.TabularInline):
    model = Subcategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    inlines = (SubcategoryInLine,)
    list_display = (
        'id', 'name', 'slug', 'image',
    )


@admin.register(Subcategory)
class SubcategoryAdmin(BaseAdmin):
    list_display = (
        'id', 'name', 'slug', 'image', 'category',
    )
    list_editable = (
        'category',
    )
    list_filter = (
        'category',
    )
