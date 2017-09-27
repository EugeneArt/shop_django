from django.http import JsonResponse
from products.models import Product

def put_product_in_basket(request):
    return_dict = dict()
    data = request.POST
    product_id = data.get("product_id")

    if ('pruducts' in request.session):
        array_of_id = request.session['pruducts'].split(",")

        if (product_id in array_of_id):
            request.session[product_id] = int(request.session[product_id]) + 1
        else:
            request.session['pruducts'] = request.session['pruducts'] + ',' + product_id
            array_of_id.append(product_id)
            request.session[product_id] = 1

        products = Product.objects.filter(pk__in=array_of_id)
        total_price = 0
        for item in products:
            count = int(request.session.get(str(item.id)))
            total_price += item.price * count

        request.session['total_price'] = str(total_price)
        return_dict["total_price"] = total_price
    else:
        product = Product.objects.get(pk=product_id)
        request.session['pruducts'] = product_id
        request.session[product_id] = 1
        request.session['total_price'] = str(product.price)

        return_dict["total_price"] = product.price

    return JsonResponse(return_dict)

def clear_basket(request):
    if ('pruducts' in request.session):
        array_of_id = request.session['pruducts'].split(",")
        for key in array_of_id:
            if(key in request.session):
                del request.session[key]

        del request.session['pruducts']
        del request.session['total_price']

    return JsonResponse({'status': 'ok'})
