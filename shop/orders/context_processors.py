
def products_in_basket(request):
    context_data = dict()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if (request.session.get('total_price')):
        total_price = request.session['total_price']
    else:
        total_price = 0

    context_data['total_price'] = total_price
    return context_data
