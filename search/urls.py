from django.urls import re_path as url
from .views import do_search

urlpatterns = [
    url(r'^$', do_search, name='search')
]