from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('create/', views.ProductCreateView, name='product-create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('buy/', views.BuyProduct, name="product-buy"),
    path('bid/', views.BidProduct, name="product-bid"),
    path('addwish/', views.AddWish, name='add-wish'),
    path('wish/', views.WishList, name='wish'),
    path('shopping/',views.ShoppingList, name='shopping'),
]