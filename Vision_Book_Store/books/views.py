from django.shortcuts import render
from .models import Book, Category

def home(request):
    books = Book.objects.all()
    best_sellers = Book.objects.filter(best_seller=True)
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'books': books,
        'best_sellers': best_sellers,
        'categories': categories
    })
