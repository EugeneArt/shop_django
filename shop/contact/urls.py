from django.conf.urls import url
from .views import ContactSuccesView

from .views import ContactView

urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^contact/success/$', ContactSuccesView.as_view(), name='contact_success'),
]