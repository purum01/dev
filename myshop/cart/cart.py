# cart.py

import math
from shop.models import Product
from coupons.models import Coupon
from .forms import CartAddProductForm

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart')
        if not self.cart:
            self.cart = self.session['cart'] = {}
        self.coupon = None


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[product.id]['product'] = product

        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            item['override_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
            yield item

    def add(self, product, quantity=1, override_quantity=False):
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':product.price}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = product.id
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session['coupon_id'] = None
        self.session['cart'] = {}
        self.save()

    def get_total_price(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())

    def has_coupon(self):
        coupon_id = self.session.get('coupon_id')
        if coupon_id:
            self.coupon =  Coupon.objects.get(id=coupon_id)
        
        return self.coupon

    def get_discount(self):
        if self.coupon:
            return math.trunc((self.coupon.discount / 100)*self.get_total_price())
        return 0

    def get_total_price_after_discount(self):
        return self.get_total_price()-self.get_discount()






