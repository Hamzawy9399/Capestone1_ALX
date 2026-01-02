from django.urls import path
from .api_views import CartAPI, CartDeleteAPI

urlpatterns = [
    path('', CartAPI.as_view()),
    path('<int:pk>/', CartDeleteAPI.as_view()),
]
