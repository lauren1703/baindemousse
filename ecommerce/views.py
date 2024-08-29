from django.shortcuts import get_object_or_404, render

from .models import Category, Product, Review
from .forms import EnquiryForm


def home_view(request):
    return render(request, 'ecommerce/home.html', {
        'featured_products': Product.objects.filter(featured=True)
    })

def shop_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'ecommerce/products/shop.html', {
        'category': category,
        'products': Product.objects.filter(category=category)
    })

def shop_all_view(request):
    return render(request, 'ecommerce/products/shop.html', {
        'category': "All Products",
        'products': Product.objects.all()
    })

def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'ecommerce/products/product.html', {
        'product': product,
        'reviews': Review.objects.filter(product=product)
    })

def custom_view(request):
    if request.method == 'POST':
        customForm = EnquiryForm(request.POST, request.FILES)
        if customForm.is_valid():
            customForm.save()

            return render(request, 'about/enquiry_confirm.html', {
            })
    else:
        customForm = EnquiryForm()

        return render(request, 'ecommerce/products/custom.html', {
            'form': customForm
        })

def our_brand_view(request):
    return render(request, 'about/our_brand.html', {
    })

def our_giving_view(request):
    return render(request, 'about/our_giving.html', {
    })

def contact_view(request):
    if request.method == 'POST':
        enquiryForm = EnquiryForm(request.POST)
        if enquiryForm.is_valid():
            enquiryForm.save()

            return render(request, 'about/enquiry_confirm.html', {
            })
    else:
        enquiryForm = EnquiryForm()

        return render(request, 'about/contact.html', {
            'form': enquiryForm
        })

def faq_view(request):
    return render(request, 'about/faq.html', {
    })

