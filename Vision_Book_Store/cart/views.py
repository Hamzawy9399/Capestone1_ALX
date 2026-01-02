from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from books.models import Book

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.book.price * item.quantity for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('cart')
