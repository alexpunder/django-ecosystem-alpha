from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from src.constants import MAX_PRODUCT_IMAGES
from .models import Product, ProductImage, Category, Subcategory


class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        current_images = self.instance.images.count()
        deleted_forms = none_forms = empty_forms = 0

        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                deleted_forms += 1
            if form.cleaned_data.get('id') is None:
                none_forms += 1
            if form.cleaned_data == {}:
                empty_forms += 1

        if current_images + none_forms - deleted_forms - empty_forms > 3:
            raise ValidationError(
                f'Нельзя добавлять больше {MAX_PRODUCT_IMAGES} '
                'изображений к товару.'
            )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet
    extra = 0


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
