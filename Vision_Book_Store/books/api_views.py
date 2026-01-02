from rest_framework import generics, permissions
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BestSellerAPI(generics.ListAPIView):
    queryset = Book.objects.filter(best_seller=True)
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookAdminAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryAdminAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
