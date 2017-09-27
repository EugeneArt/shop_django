from django.conf.urls import url
from landing.views import ProductList


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='home'),
]