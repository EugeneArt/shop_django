from django.conf.urls import url
from products.views import ProductList, ProductDetail, CategoryProductList, SubcategoryProductList, ProductComment


urlpatterns = [
    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/(?P<product_category>\w+)/$', CategoryProductList.as_view(), name='products_category'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/$', SubcategoryProductList.as_view(), name='products_subcategory'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/(?P<pk>\w+)/$', ProductDetail.as_view(),
        name='product'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/(?P<pk>\w+)/comment/$', ProductComment.as_view(),
        name='product_comment'),
]