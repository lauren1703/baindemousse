from django.urls import path

from . import views

app_name = 'ecommmerce'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('shop/all/', views.shop_all_view, name='all_view'),
    path('shop/<slug:category_slug>/', views.shop_view, name='shop_view'),
    path('product/<slug:slug>/', views.product_view, name='product_view'),
    path('customise-your-own/', views.custom_view, name='custom_view'),
    path('our-brand/', views.our_brand_view, name='our_brand_view'),
    path('our-giving/', views.our_giving_view, name='our_giving_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('faq/', views.faq_view, name='faq_view'),
]