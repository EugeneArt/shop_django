from django.contrib import admin
from .models import Order, ProductInOrder

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    readonly_fields = ('sub_total','amount')
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price',)
    list_display = ['customer_address', 'comments','is_active']
    inlines = [ProductInOrderInline]
    list_filter = ['is_active']


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'amount']


