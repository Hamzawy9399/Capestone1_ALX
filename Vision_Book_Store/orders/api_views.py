from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from cart.models import CartItem

class OrdersAPI(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CheckoutAPI(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        items = CartItem.objects.filter(user=self.request.user)
        total = sum(item.book.price * item.quantity for item in items)
        serializer.save(user=self.request.user, total_price=total)
        items.delete()
