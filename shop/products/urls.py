from django.conf.urls import url
from products.views import ProductList, ProductDetail, CategoryProductList, SubcategoryProductList


urlpatterns = [
    url(r'^product/(?P<pk>\w+)/$', ProductDetail.as_view(), name='product'),
    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/(?P<product_category>\w+)/$', CategoryProductList.as_view(), name='products_category'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/$', SubcategoryProductList.as_view(), name='products_subcategory'),
]