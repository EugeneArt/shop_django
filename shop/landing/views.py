from django.views.generic import ListView
from products.models import ProductImage

class ProductList(ListView):
    model = ProductImage
    template_name = 'landing/home.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)

        products_images = ProductImage.objects.filter(is_main=True)
        products_for_men = products_images.filter(product__subcategory__category__category_name='Men')[:4]
        products_for_woman = products_images.filter(product__subcategory__category__category_name='Woman')[:4]

        context['products_for_men'] = products_for_men
        context['products_for_woman'] = products_for_woman
        return context