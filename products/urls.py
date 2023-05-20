from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view/', view_products, name='view_products'),
    path('add/', add_product, name='add_product'),
    path('update/<int:id>', update_product, name='update_product'),
    path('delete/<int:id>', delete_product, name='delete_product')
]