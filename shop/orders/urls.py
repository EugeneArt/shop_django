from django.conf.urls import url
from orders.views import CartView, CartClearView


urlpatterns = [
    url(r'^put_product_in_basket', CartView.as_view(), name='put_product_in_basket'),
    url(r'^clear_basket', CartClearView.as_view(), name='clear_basket'),
]