import json
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from account.models import UserBase
from cart.cart import Cart


def get_total(request):
    user = UserBase.objects.get(username=request.user)
    cart = Cart(request)
    print(cart.get_subtotal_price())
    total = cart.get_subtotal_price() + user.shipping + user.donation
    return round(total, 2)

def get_total_before_donation(request):
    user = UserBase.objects.get(username=request.user)
    cart = Cart(request)
    total = cart.get_subtotal_price() + user.shipping
    return round(total, 2)

def get_donation(request, percent):
    cart = Cart(request)
    donation = cart.get_subtotal_price() * Decimal(percent)
    return round(donation, 2)

def get_charity(request):
    user = UserBase.objects.get(username=request.user)
    cart = Cart(request)
    return cart.get_charity_subtotal() + user.donation

@login_required
def shipping_view(request):
    user = UserBase.objects.get(username=request.user)
    user.shipping = Decimal(4)
    user.save()
    return render(request, 'payment/shipping.html', {
        'shipping_cost': user.shipping,
        'total_cost': get_total_before_donation(request),
    })

@login_required 
def delivery(request):
    if request.method == 'POST':
        user = UserBase.objects.get(username=request.user)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.address = request.POST.get('address')
        user.unit_number = request.POST.get('unitno')
        user.postcode = request.POST.get('postcode')
        user.contact_number = request.POST.get('phonenumber')
        if request.POST.get('anytime', False):
            user.dateby = 'anytime'
        else:
            user.dateby = request.POST.get('datedelivery')
        user.donation = get_donation(request, 0.05)
        user.save()
        return render(request, 'payment/payment.html', {
            'shipping': "delivery",
            'shipping_cost': user.shipping,
            'total_cost': get_total(request),
            'donation_cost': user.donation,
            'donation_percent': user.donation_percent,
            'charity': get_charity(request),
        })
    
    return render(request, 'payment/shipping.html')

@login_required
def self_collect(request):
    if request.method == 'POST':
        user = UserBase.objects.get(username=request.user)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.contact_number = request.POST.get('phonenumber')
        if request.POST.get('anytime', False):
            user.dateby = 'anytime'
        else:
            user.dateby = request.POST.get('datepickup')
        user.donation = get_donation(request, 0.05)
        user.save()
        return render(request, 'payment/payment.html', {
            'shipping': "self-collect",
            'shipping_cost': user.shipping,
            'total_cost': get_total(request),
            'donation_cost': user.donation,
            'donation_percent': user.donation_percent,
            'charity': get_charity(request),
        })
    
    return render(request, 'payment/shipping.html')

def shipping_update(request):
    user = UserBase.objects.get(username=request.user)
    if request.POST.get('action') == 'delivery':
        user.shipping = Decimal(4)
    else:
        user.shipping = Decimal(0)
    user.save()
    response = JsonResponse({'shippingcost': user.shipping, 'total': get_total_before_donation(request)})
    return response

def donation_update(request):
    user = UserBase.objects.get(username=request.user)
    if request.POST.get('custom'):
        user.donation = round(Decimal(request.POST.get('custom')), 2)
        user.donation_percent = "custom"
    elif request.POST.get('donation') == '5':
        user.donation = get_donation(request, 0.05)
        user.donation_percent = "5%"
    elif request.POST.get('donation') == '10':
        user.donation = get_donation(request, 0.1)
        user.donation_percent = "10%"
    elif request.POST.get('donation') == '15':
        user.donation = get_donation(request, 0.15)
        user.donation_percent = "15%"
    elif request.POST.get('donation') == '20':
        user.donation = get_donation(request, 0.2)
        user.donation_percent = "20%"
    else:
        user.donation = 0
        user.donation_percent = "none"
    user.save()
    response = JsonResponse({'donationcost': user.donation, 'donationpercent': user.donation_percent, 'total': get_total(request), 'charity': get_charity(request),})
    return response
