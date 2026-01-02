from django.urls import path
from .views import cart_view, add_to_cart

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:book_id>/', add_to_cart),
]
