from django.template import Template, Context
from django.core.mail import send_mail
from shop.celery import app
from orders.models import Order

REPORT_TEMPLATE = """
Orders:

{% for order in orders %}
        Order price: {{ order.total_price }}
        Customer name, email, phone:  {{ order.customer_name }} , {{ order.customer_email }}, {{ order.customer_phone }}
        Customer addres: {{ order.customer_address }}
        Comment to order: {{ order.comments }}
{% endfor %}
"""


@app.task
def send_orders():

    orders = Order.objects.filter(is_active=True)

    template = Template(REPORT_TEMPLATE)

    send_mail(
        'Orders from shop',
        template.render(context=Context({'orders': orders})),
        'test@gmail.com',
        ['client@mail.ru'],
        fail_silently=False,
    )