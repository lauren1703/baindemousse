from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from account.models import UserBase
from cart.cart import Cart
from payment.views import get_charity, get_total

from .models import Order, OrderItem


@login_required
def place_order(request):
    if request.method == 'POST':
        total = get_total(request)
        cart = Cart(request)
        user = UserBase.objects.get(username=request.user)
        order = Order.objects.create(user_id = request.user.id,
                    full_name = user.first_name + " " + user.last_name,
                    address = user.address,
                    unit_no = user.unit_number,
                    postcode = user.postcode,
                    phone = user.contact_number,
                    email = user.email,
                    total = get_total(request),
                    subtotal = cart.get_subtotal_price(),
                    shipping = user.shipping,
                    donation = user.donation,
                    donation_percent = user.donation_percent,
                    charity = get_charity(request),
                    dateby = user.dateby,
                    shipping_method = request.POST.get('shipping'),
                    payment_method = request.POST.get('vbtn-radio'),)
        order_id = order.pk
        for item in cart:
            OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
            item['product'].stock = item['product'].stock - 1
            item['product'].save()

        cart.clear()
        
        if request.POST.get('vbtn-radio') == 'paynow':
            return render(request, 'orders/paynow_instructions.html', {
                'total': total,
                'order': order
            })
        else:
            order_confirm(request, order_id, total)
    
    return order_confirm(request, order_id, total)

def order_confirm(request, order_id, total):
    order = Order.objects.get(pk = order_id)
    user = UserBase.objects.get(username=request.user)
    current_site = get_current_site(request)
    subject = 'Bain de Mousse Order Confirmation'
    message = render_to_string('orders/order_confirm_email.html', {
        'user': user,
        'domain': current_site.domain,
        'order': order
    })
    user.email_user(subject=subject, message=message)

    return render(request, 'orders/order_confirm.html', {
                'total': total,
                'order': order
            })

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    return orders

def view_order(request, order_id):
    order = Order.objects.get(pk = order_id)
    return render(request, 'orders/view_order.html', {
                'order': order,
            })
