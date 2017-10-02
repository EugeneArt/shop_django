from django.conf.urls import url, include
from orders.views import CartView, CartClearView, OrderListView, OrderCheckoutView, OrderSuccessView


urlpatterns = [
    url(r'^put_product_in_basket/$', CartView.as_view(), name='put_product_in_basket'),
    url(r'^clear_basket/$', CartClearView.as_view(), name='clear_basket'),
    url(r'^order/', include([
        url(r'^$', OrderListView.as_view(), name='order'),
        url(r'^checkout/$', OrderCheckoutView.as_view(), name='order_checkout'),
        url(r'^success/$', OrderSuccessView.as_view(), name='order_success'),
    ])),
]