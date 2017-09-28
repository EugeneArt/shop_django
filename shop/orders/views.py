from django.http import JsonResponse
from django.shortcuts import render

from products.models import Product, ProductImage
from orders.models import ProductInOrder

from django.views import View
from django.views.generic.edit import FormView

from .forms import OrderForm


class CartView(View):

    def post(self, request):

        return_dict = dict()

        # modified dictionary for session
        request.session.modified = True

        #get id of product from ajax response
        data = request.POST
        product_id = data.get("product_id")

        #add product in session order
        if('order' in request.session):
            if(product_id in request.session['order']):
                request.session['order'][str(product_id)] = int(request.session['order'][str(product_id)]) + 1
            else:
                request.session['order'][str(product_id)] = 1
        else:
            request.session['order'] = dict.fromkeys(product_id, 1)

        #count total price for order
        total_price = 0
        products = Product.objects.filter(pk__in=request.session['order'].keys())
        for product in products:
            total_price += product.price * int(request.session['order'].get(str(product.id)))

        #save total price in session and send price to front
        request.session['order_price'] = str(total_price)
        return_dict["order_price"] = total_price

        return JsonResponse(return_dict)

class CartClearView(View):

    def post(self, request):
        if ('order' in request.session):
            del request.session['order']
            del request.session['order_price']

        return JsonResponse({'status': 'cart is clear'})

class OrderListView(View):
    template_name = 'orders/order.html'

    def get(self, request, *args, **kwargs):
        if ('order' in request.session):
            #get products in session and fill empty products fields
            products = Product.objects.filter(pk__in=request.session['order'].keys())
            for product in products:
                product.amount = request.session['order'][str(product.id)]
                product.sub_total = product.price * int(product.amount)
                product.main_image = ProductImage.objects.get(product__pk=product.id, is_main=True)
        else:
            products = None
        return render(request, self.template_name, {'products': products})

    def post(self, request, *args, **kwargs):

        # modified dictionary for session
        request.session.modified = True

        # get id and amount of products from ajax response
        data = request.POST
        product_id = data.get("product_id")
        amount = data.get("amount")

        # set amount of product in session
        request.session['order'][str(product_id)] = amount

        # count total price for order
        total_price = 0
        products = Product.objects.filter(pk__in=request.session['order'].keys())
        for product in products:
            total_price += product.price * int(request.session['order'].get(str(product.id)))

        #save total price in session
        request.session['order_price'] = str(total_price)

        return JsonResponse({'order_price': total_price})

class OrderCheckoutView(FormView):
    template_name = 'orders/order-form.html'
    form_class = OrderForm
    success_url = '/success-order/'

    def get_initial(self):
        initial = super(OrderCheckoutView, self).get_initial()

        initial['total_price'] = self.request.session['order_price']
        return initial

    def form_valid(self, form):
        order = form.save()

        #fill products in order for Order in session
        for id, amount in self.request.session['order'].items():
            product = Product.objects.get(pk=id)
            sub_total = product.price * int(amount)
            product_in_order = ProductInOrder(product=product, order=order, amount=amount, sub_total=sub_total)
            product_in_order.save(force_insert=True)

        return super(OrderCheckoutView, self).form_valid(form)


