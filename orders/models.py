from decimal import Decimal

from django.conf import settings
from django.db import models

from ecommerce.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    unit_no = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=5, decimal_places=2)
    donation = models.DecimalField(max_digits=10, decimal_places=2)
    charity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dateby = models.CharField(max_length=100, blank=True)

    donation_choices = (('5', '5%'),
                        ('10', '10%'),
                        ('15', '15%'),
                        ('20', '20%'),
                        ('custom', 'Custom'),
                        ('none', 'None'),)

    donation_percent = models.CharField(max_length = 100, choices = donation_choices, default="5")

    shipping_methods = (('delivery', 'Delivery with NinjaVan'),
                        ('self-collect', 'Self-collection'),
                        )
    shipping_method = models.CharField(max_length = 100, choices = shipping_methods, default="delivery")

    payment_methods = (('paynow', 'PayNow/PayLah'),
                        ('cash', 'Cash'))
    payment_method = models.CharField(max_length = 100, choices = payment_methods, default="paynow")


    status_choices = (('received', 'Received'),
                    ('scheduled', 'Scheduled'), 
                    ('shipped', 'Shipped'),
                    ('processing','Processing'),
                    )
    status = models.CharField(max_length = 100, choices = status_choices, default="processing")
    

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
