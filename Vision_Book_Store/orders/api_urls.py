from django.urls import path
from .api_views import OrdersAPI, CheckoutAPI

urlpatterns = [
    path('', OrdersAPI.as_view()),
    path('checkout/', CheckoutAPI.as_view()),
]
