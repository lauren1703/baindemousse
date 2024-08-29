from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from ecommerce.models import Product

from .cart import Cart


def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {
        'cart': cart
    })

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(str(request.POST.get('productid')))
        product_qty = int(str(request.POST.get('productqty')))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(str(request.POST.get('productid')))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_subtotal_price()
        charitytotal = carttotal / 4
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal, 'charitytotal': charitytotal})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(str(request.POST.get('productid')))
        product_qty = int(str(request.POST.get('productqty')))
        cart.update(product=product_id, qty=product_qty)
        cartqty = cart.__len__()
        carttotal = cart.get_subtotal_price()
        charitytotal = carttotal / 4
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal, 'charitytotal': charitytotal})
        return response


def shipping_view(request):
    return render(request, 'payment/shipping.html')

def payment_view(request):
    return render(request, 'payment/payment.html')
