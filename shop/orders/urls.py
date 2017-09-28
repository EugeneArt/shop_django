from django.conf.urls import url
from orders.views import CartView, CartClearView, OrderListView, OrderCheckoutView


urlpatterns = [
    url(r'^put_product_in_basket/$', CartView.as_view(), name='put_product_in_basket'),
    url(r'^clear_basket/$', CartClearView.as_view(), name='clear_basket'),
    url(r'^order/$', OrderListView.as_view(), name='order'),
    url(r'^order/checkout/$', OrderCheckoutView.as_view(), name='order_checkout'),
]