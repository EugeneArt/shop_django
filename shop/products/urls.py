from django.conf.urls import url, include
from products.views import ProductList, ProductDetail, CategoryProductList, SubcategoryProductList, ProductCommentCreate, TagIndexView, SearchListView, SearchAutocompleteView, ProductCommentList

urlpatterns = [
    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/(?P<product_category>\w+)/$', CategoryProductList.as_view(), name='products_category'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/$', SubcategoryProductList.as_view(), name='products_subcategory'),
    url(r'^products/(?P<product_category>\w+)/(?P<product_subcategory>\w+)/(?P<pk>\w+)/', include([
            url( r'^$', ProductDetail.as_view(), name = 'product'),
            url(r'^comment/$', ProductCommentCreate.as_view(), name='product_comment'),
            url(r'^comments/$', ProductCommentList.as_view(), name='product_comments'),

        ])),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
    url(r'^search/$', SearchListView.as_view(), name='search'),
    url(r'^autocomplete/$', SearchAutocompleteView.as_view(), name='autocomplete'),
]

