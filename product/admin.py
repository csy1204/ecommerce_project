from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','status','price','seller']
    list_filter=['status']
    search_fields=['name']

admin.site.register(Product, ProductAdmin)