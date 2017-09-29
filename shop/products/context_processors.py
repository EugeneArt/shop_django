from .models import Category

def products_catecory_context(request):
    context_data = dict()

    context_data['categories'] = Category.objects.all()
    return context_data
