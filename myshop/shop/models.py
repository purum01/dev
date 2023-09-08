from django.db import models
from django.urls import reverse

class Category(models.Model):
    id = models.CharField(max_length=200, db_index=True, primary_key=True )
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.id])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    id = models.CharField(max_length=200, db_index=True, primary_key=True )
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id])