from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm
from datetime import datetime
from django.utils import timezone

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

def ProductCreateView(request):
    if request.method == 'POST':                                                          
        product_form = ProductForm(request.POST)         
        print("진입")                                         
        if product_form.is_valid():
            print("valid")
            new_product = product_form.save(commit=False)                                             #commit=False -> 데이터베이스에 넘기지 않음 객체만 만들어짐
            new_product.seller = request.user 
            # naive datetime -> UTC +9:00 으로 변환                    
            new_product.end_time = timezone.make_aware(datetime.strptime(request.POST['end_time'], "%Y/%m/%d %H:%M"))
            new_product.save()                 
            return HttpResponseRedirect('/product')
        print("not valid")
    else:
        product_form = ProductForm()                                                              

    return render(request, 'product_create.html',{'form':product_form})


def BuyProduct(request):
    """
    물건 구매
    params: Product_id
        Product.status을 3으로 변환
    redirect: Product Detail
    """
    product = Product.objects.get(pk=request.GET.get('id',1))
    product.status = 3
    product.save()
    return HttpResponseRedirect('/product/'+request.GET.get('id'))


def BidProduct(request):
    """

    """
    pass


def WishList(request):
    pass
