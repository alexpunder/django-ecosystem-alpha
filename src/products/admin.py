from django.contrib import admin

from .models import Product, ProductImage, Category, Subcategory


class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    inlines = (ProductImageInline,)


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(BaseAdmin):
    pass
