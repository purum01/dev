from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','category','price','stock','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','stock','available']