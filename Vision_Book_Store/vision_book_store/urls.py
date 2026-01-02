from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('api/books/', include('books.api_urls')),
    path('api/cart/', include('cart.api_urls')),
    path('api/orders/', include('orders.api_urls')),
]
