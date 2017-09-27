from django.views.generic import ListView, DetailView
from products.models import Product, ProductImage

class ProductList(ListView):
    model = ProductImage
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['title'] = 'Products'
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'

class CategoryProductList(ListView):
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        products = ProductImage.objects.filter(product__subcategory__category__category_name=self.kwargs['product_category'],
                                               is_main=True)
        return products

    def get_context_data(self, **kwargs):
        context = super(CategoryProductList, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['product_category']
        return context

class SubcategoryProductList(ListView):
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        products = ProductImage.objects.filter(product__subcategory__category__category_name=self.kwargs['product_category'],
                                               is_main=True) \
                                        .filter(product__subcategory__subcategory_name=self.kwargs['product_subcategory'])
        return products

    def get_context_data(self, **kwargs):
        context = super(SubcategoryProductList, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['product_category']
        context['title'] = self.kwargs['product_subcategory']
        return context

