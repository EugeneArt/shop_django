from django.contrib import admin
from .models import Order, ProductInOrder

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price','customer_address', 'comments','is_active']
    inlines = [ProductInOrderInline]

@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'amount']

