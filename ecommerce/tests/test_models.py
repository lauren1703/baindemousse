from django.test import TestCase

from ecommerce.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Bath Bombs', slug='bath-bombs')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Bath Bombs')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Bath Bombs', slug='bath-bombs')
        self.data1 = Product.objects.create(category_id=1, title='Simply Lavender', slug='simply-lavender', price='8', image='lavender')  

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Simply Lavender')