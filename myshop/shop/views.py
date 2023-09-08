from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',{'product':product,'cart_product_form':cart_product_form})

def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request,'shop/product/list.html',{'category':category, 'categories':categories, 'products':products})