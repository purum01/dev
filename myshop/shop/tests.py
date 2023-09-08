from django.test import TestCase
from .models import Category

# Create your tests here.


class CategoryModelTests(TestCase):
    def test_Category(self):
        categories = Category.objects.all()
        print(categories)

