from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.place_order, name='place_order'),
    path('order-confirmation/<int:order_id>/<str:total>', views.order_confirm, name='order_confirm'),
    path('view-order/<int:order_id>', views.view_order, name='view_order'),
]