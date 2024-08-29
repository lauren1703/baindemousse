from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
    path('shipping/', views.shipping_view, name='shipping_view'),
    path('payment/', views.payment_view, name='payment_view')
]