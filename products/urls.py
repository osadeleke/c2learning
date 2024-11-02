from django.urls import path
from .views import product_list

urlpatterns = [
    path('listproducts/', product_list, name='product-list'),
]