from django.urls import path
from django.contrib.auth import views as auth_view
from .views import ProductList, ProductCreateView, ProductDetailView, BuyProduct

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('create/', ProductCreateView, name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buy/', BuyProduct, name="product-buy")
]