from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product
from django.urls import reverse_lazy


class ProductList(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name='product_list.html'
    def get_queryset(self):
        if self.request.user.is_buyer():
            return Product.objects.all()
        # 현재 접속자가 Seller인 경우 본인 판매 물건만
        return Product.objects.filter(seller=self.request.user)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name='product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ('name', 'phone_number', 'trading_place', 'status', 'price', 'image', 'end_time')
    success_url = reverse_lazy('products')

