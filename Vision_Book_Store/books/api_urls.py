from django.urls import path
from .api_views import BookListAPI, BestSellerAPI, BookAdminAPI, CategoryAdminAPI

urlpatterns = [
    path('', BookListAPI.as_view()),
    path('best-sellers/', BestSellerAPI.as_view()),
    path('categories/', CategoryAdminAPI.as_view()),
    path('<int:pk>/', BookAdminAPI.as_view()),
]
