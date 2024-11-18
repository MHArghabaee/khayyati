from django.urls import path
from .views import order_list, add_order

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add', add_order, name='add_order'),
]
