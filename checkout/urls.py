from django.urls import re_path as url
from .views import checkout,payment

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^payment/', payment, name='payment'),
]