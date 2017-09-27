from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^put_product_in_basket', views.put_product_in_basket, name='put_product_in_basket'),
    url(r'^clear_basket', views.clear_basket, name='clear_basket'),
]