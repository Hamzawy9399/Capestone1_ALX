from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from cart.models import CartItem

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})

@login_required
def checkout_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.book.price * item.quantity for item in items)
    Order.objects.create(user=request.user, total_price=total)
    items.delete()
    return redirect('orders')
