from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .models import *
from cart.cart import Cart
from .forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            coupon = cart.has_coupon()
            if coupon:
                order.coupon = coupon
                order.discount = coupon.discount
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()

            return render(request,'orders/order/created.html',{'order':order})
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart':cart,'form':form})


@staff_member_required
def admin_order_detail(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html',{'order':order})
