from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

#class ProductManager(models.Manager):
#    def get_queryset(self):
#        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', default="/")

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('ecommerce:shop_view', args=[self.slug])   

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=8)
    stock = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)
    small_in_stock = models.BooleanField(default=True)
    small_stock = models.IntegerField(default=0)
    small_price = models.DecimalField(max_digits=4, decimal_places=2, default=4)
    mini_in_stock = models.BooleanField(default=True)
    mini_stock = models.IntegerField(default=0)
    mini_price = models.DecimalField(max_digits=4, decimal_places=2, default=1.5)
    objects = models.Manager()
#    products = ProductManager()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('ecommerce:product_view', args=[self.slug])   
    
    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE, null=True)
    customer = models.CharField(max_length=255)
    date = models.DateField(blank=True)
    rating = models.IntegerField(default=5)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='reviews/')

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ('-date',) 
    
    def __str__(self):
        return self.customer

class Enquiry(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=8, default=0)
    enquiry = models.TextField()
    image = models.ImageField(upload_to='enquiries/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'enquiries'
        ordering = ('-date',) 

    def __str__(self):
        return self.firstname + self.lastname