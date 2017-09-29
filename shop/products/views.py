from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import ProductCommentForm
from .models import Product, ProductImage



class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['product_category']
        context['title'] = self.kwargs['product_subcategory']
        return context

class ProductComment(FormView):
    template_name = 'products/product-comment.html'
    form_class = ProductCommentForm
    success_url = '/thanks/'

    def form_valid(self, form):

        return super(ProductComment, self).form_valid(form)

class ProductList(ListView):
    model = ProductImage
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['title'] = 'Products'
        return context

class CategoryProductList(ProductList):

    def get_queryset(self):
        products = ProductImage.objects.filter(product__subcategory__category__category_name=self.kwargs['product_category'],
                                               is_main=True)
        return products

    def get_context_data(self, **kwargs):
        context = super(CategoryProductList, self).get_context_data(**kwargs)
        context['title'] = self.kwargs['product_category']
        return context

class SubcategoryProductList(ProductList):

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

