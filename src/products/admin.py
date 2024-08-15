from django.contrib import admin

from .models import Product, ProductImage, Category, Subcategory


class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class SubcategoryInLine(admin.TabularInline):
    model = Subcategory
    extra = 1


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
