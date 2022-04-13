from django.urls import re_path as url, include
from .views import all_products

urlpatterns = [
    url(r'^$', all_products, name='products')
    ]