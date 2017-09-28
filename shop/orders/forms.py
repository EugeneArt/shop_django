from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['total_price', 'customer_name', 'customer_email','customer_phone','customer_address', 'comments']