from .models import Product
from django import forms
from django.utils import timezone


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Name"
        self.fields['phone_number'].widget.attrs['placeholder'] = "Phone Number"
        self.fields['trading_place'].widget.attrs['placeholder'] = "Write Your Trading Place"
        self.fields['price'].widget.attrs['placeholder'] = "Price"         
        self.fields['price'].widget.attrs['value'] = 0 
        self.fields['end_time'] = forms.DateTimeField(label='옥션 기한', initial=timezone.localtime().strftime('%Y/%m/%d %H:%M'), input_formats=['%Y/%m/%d %H:%M', ])

    class Meta:                                                                       
        model = Product
        fields = ['name', 'phone_number', 'trading_place', 'status','longitude','latitude', 'price', 'image']
