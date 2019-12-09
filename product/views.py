from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib import messages


from .models import Product, AuctionHistory
from django.urls import reverse_lazy
from .forms import ProductForm
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin       #권한 제한하는 건데 @login_required라는 decorator는 함수형 (def)뷰에서 사용 지금은 클래스 형 뷰->Mixin사용
from accounts.models import User

def ProductList(request):
    if request.method == "GET":
        product_list= Product.objects.all() if request.user.is_buyer() else Product.objects.filter(seller=request.user)
        # 현재 접속자가 Seller인 경우 본인 판매 물건만
    else:
        # Seller name, Product name, hope price,
        filter_params = {key: value for key, value in request.POST.items() if key != 'csrfmiddlewaretoken' and value}
        product_list= Product.objects.filter(**filter_params)
        print(filter_params, product_list)

    return render(request, 'product_list.html', {"product_list": product_list} )

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name='product_detail.html'

def ProductCreateView(request):
    if request.method == 'POST':                                                          
        product_form = ProductForm(request.POST)
        print(request.POST['price'], request.POST['status'])
        if int(request.POST['price']) == 0 and int(request.POST['status'])==2:
            messages.error(request, '입력이 잘못되었습니다.')
            return render(request, 'product_create.html',{'form':product_form})                                   
        if product_form.is_valid():
            print("!!")
            new_product = product_form.save(commit=False)                                             #commit=False -> 데이터베이스에 넘기지 않음 객체만 만들어짐
            new_product.seller = request.user 
            # naive datetime -> UTC +9:00 으로 변환                    
            new_product.end_time = timezone.make_aware(datetime.strptime(request.POST['end_time'], "%Y/%m/%d %H:%M"))
            new_product.save()                 
            return HttpResponseRedirect('/product') 
    else:
        product_form = ProductForm()
                                                                  

    return render(request, 'product_create.html',{'form':product_form})


def ProductUpdateView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    print(pk, form)
    if form.is_valid():
        print("valid")
        u_product = form.save(commit=False)
        u_product.end_time = timezone.make_aware(datetime.strptime(request.POST['end_time'], "%Y/%m/%d %H:%M"))
        u_product.save()
        return redirect('/product/{}'.format(pk))
    print("not Valid")
    return render(request, 'product_create.html', {'form':form})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product-delete.html'
    success_url = reverse_lazy('products')

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
    Bid Auction
    """
    bid_product = Product.objects.get(pk=request.GET.get('id',1))
    bid_price = int(request.GET.get('bid_price'))
# if not product.is_auction_end():
    if bid_price  > bid_product.price:
        bid_product.price = bid_price 
        bid_product.winner = request.user
        AuctionHistory.objects.create(product=bid_product, bidder=request.user, price=bid_price)
        bid_product.save()
    return HttpResponseRedirect('/product/'+request.GET.get('id'))
    

def AddWish(request):
    wish_product = Product.objects.get(pk=request.GET.get("id"))
    if request.user not in wish_product.wish.all():
        wish_product.wish.add(request.user)
    return HttpResponseRedirect('/product/'+request.GET.get('id'))

def AddCart(request):
    cart_product = Product.objects.get(pk=request.GET.get("id"))
    if request.user not in cart_product.cart.all():
        cart_product.cart.add(request.user)
    return HttpResponseRedirect('/product/'+request.GET.get('id'))

def WishList(request):
    cuurent_user = User.objects.get(pk=request.user)
    wlist = cuurent_user.wish_list.all()
    return render(request, 'product_wish.html', {'wishes' :wlist})

def ShoppingList(request):
    cuurent_user = User.objects.get(pk=request.user)
    clist = cuurent_user.cart_list.filter(status=2)
    auction_products = Product.objects.filter(status=1, winner=request.user, end_time__lte=timezone.localtime())
    clist = clist | auction_products

    price_sum = sum([p.price for p in clist])

    return render(request, 'product_shopping.html', {'carts' :clist, 'sum': price_sum, })


def BuyAllProduct(request):
    # Multiple Input 추가 및 코드 수정 필요
    print(request.GET, request.GET.getlist('idList[]'))
    if request.GET.get('idList[]'):
        for idx in request.GET.getlist('idList[]'):
            product = Product.objects.get(pk=int(idx))
            product.cart.remove(request.user)
            product.status = 3
            product.save()

    return redirect('/product/shopping/')