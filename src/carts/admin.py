from django.contrib import admin

from .models import Cart, CartItem


class CartItemInLine(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInLine,)
    list_display = (
        'id', 'user',
    )
    search_fields = (
        'user__username',
    )
