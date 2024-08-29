from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.shipping_view, name='shipping_view'),
    path('delivery/', views.delivery, name='delivery'),
    path('self-collect/', views.self_collect, name='self_collect'),
    path('shipping-update/', views.shipping_update, name='shipping_update'),
    path('donation-update/', views.donation_update, name='donation_update'),
]