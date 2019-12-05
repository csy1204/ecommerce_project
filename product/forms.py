from .models import Product
from django import forms
from django.utils import timezone


class ProductForm(forms.ModelForm):         
    end_time = forms.DateTimeField(label='옥션 기한', initial=timezone.localtime(), input_formats=['%Y/%m/%d %H:%M', ])
    class Meta:                                                                       
        model = Product
        fields = ['name', 'phone_number', 'trading_place', 'status', 'price', 'image']
