import math
from django.db import models
from shop.models import Product

from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon

class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='이름')
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=250, verbose_name='주소')
    tel = models.CharField(max_length=20 ,verbose_name='전화번호')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='orders',  null=True,  blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_product(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_discount(self):
        return math.trunc(self.get_total_product()*(self.discount / 100))

    def get_total_cost(self):
        total_cost = self.get_total_product()
        total_discount = self.get_total_discount()
        return math.trunc(total_cost - total_discount)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'
        
    def get_cost(self):
        return self.price * self.quantity

