from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views import View
from django.urls import reverse
from .forms import ProductCommentForm
from .models import Product, ProductImage, ProductComment
from taggit.models import Tag
from django.db.models import Q


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class ProductDetail(TagMixin, DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['product_category']
        context['title'] = self.kwargs['product_subcategory']
        context['tags'] = Tag.objects.filter(product__id=self.kwargs['pk'])
        return context

class ProductCommentCreate(FormView):
    template_name = 'products/product-comment.html'
    form_class = ProductCommentForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.product_id = self.kwargs['pk']
        instance.save()
        return super(ProductCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('product',
                       kwargs={
                           'product_category': self.kwargs['product_category'],
                           'product_subcategory': self.kwargs['product_subcategory'],
                           'pk': self.kwargs['pk'],
                       })

class ProductCommentList(TagMixin, ListView):
    model = ProductComment
    template_name = 'products/product-comments.html'
    context_object_name = 'comments'
    paginate_by = 6

    def get_queryset(self):
        comments = ProductComment.objects.filter(product__id = self.kwargs['pk'])
        return comments

    def get_context_data(self, **kwargs):
        context = super(ProductCommentList, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['product_category']
        context['subcategory'] = self.kwargs['product_subcategory']
        context['product'] = self.kwargs['pk']
        return context

class ProductList(TagMixin, ListView):
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

class TagIndexView(TagMixin, ListView):
    model = ProductImage
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return ProductImage.objects.filter(product__tags__slug=self.kwargs.get('slug'))

class SearchListView(ProductList):
    def get_queryset(self):
        query = self.request.GET['search']
        products = ProductImage.objects.filter(
                                                Q(product__name__icontains=query) |
                                                Q(product__subcategory__subcategory_name__icontains=query) |
                                                Q(product__subcategory__category__category_name__icontains=query)
                                              )
        return products

class SearchAutocompleteView(View):
    def get(self, request):
        query = request.GET['query']
        products = Product.objects.filter(
                                                Q(name__icontains=query) |
                                                Q(subcategory__subcategory_name__icontains=query) |
                                                Q(subcategory__category__category_name__icontains=query)
                                              )
        data = [product.name for product in products]
        return JsonResponse({'query': data})