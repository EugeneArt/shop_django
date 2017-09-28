from django.contrib import admin
from django.utils.html import format_html
from .models import Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price',)
    list_display = ['total_price', 'customer_address', 'comments','is_active']
    inlines = [ProductInOrderInline]
    list_filter = ['is_active']


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'amount', 'sub_total']
    readonly_fields = ('sub_total',)

    def sub_total(self, instance):
        return format_html("<span>{} $</span>",instance.amount * instance.product.price)

    sub_total.short_description = "Total price for products"



