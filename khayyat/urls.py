from django.urls import path
from .views import order_list, add_order, edit_order, delete_order

urlpatterns = [
    path('', order_list, name='order_list'),
    path('add', add_order, name='add_order'),

    path('order/edit/<int:order_id>/', edit_order, name='edit_order'),

    path('orders/delete/<int:order_id>/', delete_order, name='delete_order'),
]
