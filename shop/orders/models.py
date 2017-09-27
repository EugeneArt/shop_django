from django.db import models
from products.models import Product

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Order %s" % (self.id)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return "Product in order %s" % self.product.name

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products in order'
