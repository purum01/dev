from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/',views.order_create,name='order_create'),
    path('admin/order/<order_id>/',views.admin_order_detail,name='admin_order_detail'),
]