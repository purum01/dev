from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('',views.product_list, name='product_list'),
    path('<category_id>/',views.product_list, name='product_list_by_category'),
    path('detail/<id>/',views.product_detail, name='product_detail'),
]