from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.view_orders, name='view_orders'),
    path('orders/<int:id>/add/', views.add_order, name='add_order'),
    path('department/add', views.add_departments, name='add_department'),
    path('orders/<int:id>/delete', views.delete_order, name='delete_order')
]