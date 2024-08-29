from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from ecommerce.models import Category, Product
from ecommerce.views import home_view, shop_all_view


class  TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name='Bath Bombs', slug='bath-bombs')
        self.data1 = Product.objects.create(category_id=1, title='Simply Lavender', slug='simply-lavender', price='8', image='lavender')  

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('ecommerce:product_view', args=['simply-lavender']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('ecommerce:shop_view', args=['bath-bombs']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = home_view(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)


        
