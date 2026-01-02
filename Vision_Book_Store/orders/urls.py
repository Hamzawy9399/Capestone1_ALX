from django.urls import path
from .views import orders_view, checkout_view

urlpatterns = [
    path('', orders_view, name='orders'),
    path('checkout/', checkout_view, name='checkout'),
]
