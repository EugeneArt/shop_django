from django.http import JsonResponse
from products.models import Product
from django.views import View

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
            total_price += product.price * request.session['order'].get(str(product.id))

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
