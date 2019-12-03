from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Sell

from django.contrib.auth.mixins import LoginRequiredMixin       #권한 제한하는 건데 @login_required라는 decorator는 함수형 (def)뷰에서 사용 지금은 클래스 형 뷰->Mixin사용

class PhotoListView(LoginRequiredMixin,ListView):
    login_url='/account/login/'
    model = Sell
    template_name="selllist.html"
    